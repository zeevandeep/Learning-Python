s1='iceman'
s2='cinema'
if len(s1)!=len(s2):
    print False
else:
    for char in s1:
        if s2.find(char)==-1:
            print False
        else:
        	s2=s2.replace(char,"")

print True