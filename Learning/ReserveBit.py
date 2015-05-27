x= 0
y=[]
done = False
k=''
while not done:
	y.append(x%2)
	x=x/2
	if x==1 or x==0:
		done = True
y.append(x)
h=len(y)
r=32-h
for q in range(0,r):
	y.append(0)
t=0
w=0
y.reverse()
for u in y:
	w+=2**t*u
	t+=1
	if t==32:
		break
print w


