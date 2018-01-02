import pandas as pd
df=pd.read_csv("STG_RTBL_SHORT.csv")
rows,columns = df.shape
print df.describe
