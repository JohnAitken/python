from datetime import datetime
import itertools
import ast
import re
import itertools
from collections import Counter

import pandas as pd
import numpy as np

# https://www.kaggle.com/code/jeanmidev/overview-of-doctor-who

# Collect the scripts
all_scripts = pd.read_csv('drwhodata/all-scripts.csv')
all_scripts.sort_values(["doctorid","episodeid"],ascending = True,inplace = True)

# Add details on the type of doctor
def clean_name(row):
    clean_name = str(row["details"])
    for piece in [" [OC]","[OC]"]:
        if piece in clean_name:
            clean_name = clean_name.replace(piece,"")
    
    if "DOCTOR" in clean_name:
        return f"DOCTOR_{row['doctorid']}"
    
    return clean_name

all_scripts["details"] = all_scripts.apply(lambda row: clean_name(row) ,axis=1)




# Collect the dwGuide
dw_guide = pd.read_csv('drwhodata/dwguide.csv')

# Make some cleaning
dw_guide["AI"] = dw_guide.apply(lambda row: float(row["AI"]),axis=1)
dw_guide["views"] = dw_guide.apply(lambda row: float(row["views"].replace("m","")),axis=1)
dw_guide["date"] = dw_guide.apply(lambda row: row['broadcastdate'] + " " + row['broadcasthour'] ,axis=1)
dw_guide["broadcastdate_datetime"] = dw_guide.apply(lambda row: datetime.strptime(row['date'],"%d %b %Y %I:%M%p") ,axis=1)
dw_guide["broadcastdate_hour"] = dw_guide.apply(lambda row: row['broadcastdate_datetime'].hour,axis=1)
dw_guide["broadcastdate_year"] = dw_guide.apply(lambda row: row['broadcastdate_datetime'].year,axis=1)

#Works on the title of the episode (for the classic area)
dw_guide["title2"] = dw_guide["title"].apply(lambda x:x.split(":")[0])

# Clean the dirty string list
dw_guide["cast"] = dw_guide["cast"].apply(lambda x:ast.literal_eval(x))

dw_guide["crew"] = dw_guide["crew"].apply(lambda x:ast.literal_eval(x))



# Estimate if the episode was in the classic era or the modern era
def is_classicperiod(x):
    if x>=2005:
        return False
    return True

dw_guide["is_classicperiod"] = dw_guide["broadcastdate_year"].apply(lambda x:is_classicperiod(x))

dw_guide.sort_values(["episodenbr"], ascending = True, inplace = True)
dw_guide.reset_index(inplace = True, drop = True)

print(dw_guide.head())




# Collect the right columns for the analysis
dw_guide_cast = dw_guide[["episodenbr","title","title2","broadcastdate_datetime","broadcastdate_year","is_classicperiod","cast"]].reset_index()



# Rebuild the casting of the show
#casting = dw_guide_cast["cast"].explode().to_frame().reset_index() # Run with pandas 0.25

# Use an old trick to do it
casting = pd.DataFrame({'index':dw_guide_cast["index"].repeat(dw_guide_cast["cast"].str.len()),'cast':np.concatenate(dw_guide_cast["cast"].values)})



# Rebuild the casting of the show
casting["name"] = casting["cast"].apply(lambda x:x["name"])
casting["role"] = casting["cast"].apply(lambda x:x["role"])

# Get an uncredited flag
def is_uncredited(x):
    if "uncredited" in x:
        return True
    return False
casting["is_uncredited"] = casting["name"].apply(lambda x:is_uncredited(x))
# Drop the uncredited tag in the name
casting["name"] = casting["name"].apply(lambda x:x.replace(" (uncredited)",""))


del casting["cast"]
del dw_guide_cast["cast"]

# Upgrade the general informations on the casting
dw_guide_cast = dw_guide_cast.reset_index().merge(casting,on = ["index"])
del dw_guide_cast["index"]



# Build some statistic on the actor who played in the show (if they are bask or not etc)
agg_func = {
    "broadcastdate_year":["min","max"],
    "episodenbr":[pd.Series.nunique]
}
stats_cast = dw_guide_cast[dw_guide_cast["is_uncredited"] == False].groupby(["name"]).agg(agg_func).reset_index()
stats_cast["deltatime"] = stats_cast["broadcastdate_year","max"] - stats_cast["broadcastdate_year","min"]

stats_cast.sort_values(["deltatime"], ascending = False, inplace = True)

old_columns = stats_cast.columns
new_columns = []
for column in old_columns:
    new_columns.append(f"{column[0]}_{column[1]}")
stats_cast.columns = new_columns

# Determine if the actor start or end in the modern age of the show
def is_threshold(x, limit, is_superior = True):
    if is_superior:
        if x >= limit:
            return True
        return False
    else:
        if x <= limit:
            return True
        return False
    
stats_cast['firstappereance_ismodern'] = stats_cast["broadcastdate_year_min"].apply(lambda x:is_threshold(x, 2005))
stats_cast['lastappereance_ismodern'] = stats_cast["broadcastdate_year_max"].apply(lambda x:is_threshold(x, 2005))

stats_cast["appereance_modernage"] = stats_cast.apply(lambda x:f"FA:{x['firstappereance_ismodern']} / LA:{x['lastappereance_ismodern']}",axis = 1)



# Let's see now the actor and their count of role
count_role = dw_guide_cast[dw_guide_cast["is_uncredited"] == False].groupby(["name"]).nunique()["role"].reset_index()
count_role.sort_values(["role"], ascending = False, inplace = True)




# dw_guide_cast[dw_guide_cast["name"] == "Nicholas Briggs"]["role"].unique()

