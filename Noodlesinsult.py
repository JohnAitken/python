import random

#another comment

insult1 = {1:'tinfoilhatheaded',2:"Spaznutty",3:"Cockwomblesque",4:"Chaffcunty",5:"Flegma-faced",6:"Clodhopping"}

insult2 = {1:'chocolateman',2:"optical illusion",3:"nightmare",4:"quincunt",5:"space cadet",6:"Jesus"}

def insult():
	number1 = random.randint(1,6)
	number2 = random.randint(1,6)
	print "\n\nToday Noodles is a",insult1[number1],insult2[number2]

print("A man can be many things:\n")

#loop through all possible iterations of the insults

for i in insult1:

	r=1
	while r<7:
		print 'a',insult1[i],insult2[r]
		r+=1
	r=1

print "\n\nYet..."
insult()
