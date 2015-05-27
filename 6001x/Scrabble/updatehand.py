
hand = {'e': 1, 'g': 1, 'h': 1, 'o': 2, 's': 1, 'v': 1, 'x': 2} 
handy = hand.copy() 
word = 'shoe'
for x in word:
	for y in handy:
		if x==y:
			if handy[y]==0:
				q=5
			else:
				handy[y]-=1


print handy
print hand
