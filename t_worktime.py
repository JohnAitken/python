import re
import fnmatch
import fileinput

# github this
#an update 


with open('work_attendance.txt',"r") as f, open("outfile.txt","w") as outfile:
#if blank line, delete the line for all lines, then write the output file
 for i in f.readlines():
       if not i.strip():
           continue
       if i:
           outfile.write(i)
f.close()
results = []
#strip all but the last nine chars of each line from the output file to a list
with open('outfile.txt','r') as o:
    for line in o:
        results.append(line[-9:])
o.close()

#remove invisible newline in each item of the list
results = [x.strip(' \n') for x in results]
#split into morning and afternoon lists based on if there is a PM or AM in the last 2 chars
Afternoons = fnmatch.filter(results, '*PM')
Mornings = fnmatch.filter(results, '*AM')

Mornings = [x[:-2].rstrip() for x in Mornings]

#replace hours with hours*3600, mins with mins*60 and sum
Mornings=[x.split(':') for x in Mornings]
y = len(Mornings)
secs=[]
for x in range(y):
    a=int(Mornings[x][0]) * 3600
    b=int(Mornings[x][1]) * 60
    c=a+b
    secs.append(c)

av= sum(secs)/(len(secs)*1.0)


Afternoons = [x[:-2].rstrip() for x in Afternoons]

#replace hours with hours*3600, mins with mins*60 and sum
Afternoons=[x.split(':') for x in Afternoons]
y = len(Afternoons)
secs2=[]
for x in range(y):
    a=int(Afternoons[x][0]) * 3600
    b=int(Afternoons[x][1]) * 60
    c=a+b
    secs2.append(c)

av2 = sum(secs2)/(len(secs2)*1.0)



morn_hr=int(av/3600)
aft_hr=int(av2/3600)

morn_min=int((float(av/3600)-morn_hr) * 60)
aft_min=int((float(av2/3600)-aft_hr) * 60)

if morn_min < 10:
    morn_min = "%02d" % morn_min
else:
    morn_min=morn_min

if aft_min < 10:
    aft_min = "%02d" % aft_min
else:
    aft_min=aft_min

print 'Av start time: ',morn_hr,':',morn_min,'AM'
print 'Av quit time: ',aft_hr,':',aft_min,'PM'
