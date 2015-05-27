s='gxiiwnxcc'
k=0
z=0
big=s[0]

for i in range(0,len(s)-1):
	if s[i] < s[i+1]:
		g=s[i]
		
		for j in range(i,len(s)-1):
			if s[j] < s[j+1] or s[j] == s[j+1]:
				g+=s[j+1]
				print g
			else:
				break

		k=len(g)
		if k!=0:
			if k == z:
				break
			elif k > z:
				big=g
				z=len(big)
print("Longest substring in alphabetical order is: %s" %big)


