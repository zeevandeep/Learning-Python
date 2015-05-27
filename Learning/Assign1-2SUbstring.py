s="xyfbbobcgvbobob"
m=len(s)
g = 'qqq'
q=0
j=0
for i in range(0,m):
	#j=i+1
	k=i+2
	g=s[i:k+1]
    	if (g=="bob"):
        	q+=1
        	i+=1
        	 
        		

print("Number of times bob occurs is %d " %q)
