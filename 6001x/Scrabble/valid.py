
word='rapture' 
hand ={'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}
q=['daikon','kwijibo','hello','rapture']
handy=hand.copy()
a=''
c=0
k=0
for x in word:
	for y in hand:		
		if x==y:
			if hand[y]==0:
				break
			else:
				hand[y]-=1
				a+=x
				print a
if a in q or a =='':
	print True
else:
	print False 
