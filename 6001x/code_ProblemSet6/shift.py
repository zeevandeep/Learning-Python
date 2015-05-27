class Ceaser(object):
        def buildCoder(shift):
                a='abcdefghijklmnopqrstuvwxyz'
                b=list(input("Enter a Message"))
                d=''
                for c in b:
                        if c in a:
                                d+= a[(a.index(c)+shift)%26]
                print (d)
        def buildDecoder(shift):
                a=list('abcdefghijklmnopqrstuvwxyz')
                b=list(input("Enter to Decode"))
                d=''
                for c in b:
                        if c in a:
                                d+=a[(a.index(c)-shift)%26]
                print(d)
