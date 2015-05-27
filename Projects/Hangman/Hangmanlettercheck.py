secretWord='apple' 
lettersGuessed=['e', 'i', 'k', 'p', 'r', 's']
output= '_ pp_ e'
c=0
q=0
s=[]
k=1
q = len(secretWord)
t=[]
for h in range (0,q):
	t+='_'
	
	print t

for k in lettersGuessed:
	if k not in s:
		s.append(k)

lettersGuessed=s[:]
for x in lettersGuessed:
	k=0
	for y in secretWord:
		if x == y:
			
			"""print x"""
		
			print secretWord[k]

			t[k]=secretWord[k]
		
		k+=1
		
print ''.join(t)


"""

for x in lettersGuessed:
	for y in secretWord:
		if x == y:
    			a+=x
    			break   
print a 
for z in a:
    for w in secretWord:
        if z == w:
            c+=1
            print c


print q

if c==q:
	print True
else:
	print False

"""



