secretWord='carrot' 
lettersGuessed=['h', 'k', 'r', 'g', 'v', 'c', 'n', 'j', 'f', 'y']
output= '_ pp_ e'
c=0
q=0
s=[]
k=1
q = len(secretWord)
t=[]
l=''
for h in range (0,q):
	t+='_'
	
	"print t"

for k in lettersGuessed:
	if k not in s:
		s.append(k)

lettersGuessed=s[:]
for x in lettersGuessed:
	k=0
	for y in secretWord:
		if x == y:
			
			t[k]=secretWord[k]
		
		k+=1
for o in t:
	l+=o
print l

print " ".join(l)





