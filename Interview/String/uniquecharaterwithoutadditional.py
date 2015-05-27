a=list('abaa')
for each in a:
	c=a.count(each)
	if c>1:
		a.remove(each)
	c=0
b= ''.join(a)
print b