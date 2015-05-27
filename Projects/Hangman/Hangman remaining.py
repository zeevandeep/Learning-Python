def chec(lettersGuessed):
	a='abcdefghijklmnopqrstvwxyz'
	b=a[:]
	c=len(a)
	d=[]

	for q in range(0,c):
		d+=a[q]

	for x in lettersGuessed:
		k=0
		for y in d:
			if x==y:
			
				del d[k]
				print d
			k+=1
	return( " ".join(d))

chec(['e','a','z'])
