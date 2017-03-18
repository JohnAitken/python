import re
import fnmatch
import fileinput
import math

#local

#strip blank lines and output to outfile.txt
with open('work_attendance.txt',"r") as f, open("outfile.txt","w") as outfile:
 for i in f.readlines():
       if not i.strip():
           continue
       if i:
           outfile.write(i)
f.close()
results = []
with open('outfile.txt','r') as o:
    for line in o:
        #strip out the last 9 chars - the time plus extra chars
        results.append(line[-9:])
o.close()
#remove extra chars
results = [x.strip(' \n') for x in results]
Afternoons = fnmatch.filter(results, '*PM')
Mornings = fnmatch.filter(results, '*AM')



def average_time(timeperiod):
    av1 = [x[:-2].rstrip() for x in timeperiod]
    av2 = [y.split(':') for y in av1]
    avlen= len(av2)
    avsecs=[]
    for x in range(y):
        a=int(av2[x][0]) * 3600
        b=int(av2[x][1]) * 60
        c=a+b
        return avsecs.append(c)


average_time(Mornings)
print average_time

#av= sum(secs)/(len(secs)*1.0
