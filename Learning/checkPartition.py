class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class Element:
    def __init__(self):
        self.head=None
        self.length=0

    def insert(self,data):
        newNode=Node()
        newNode.setData(data)


        if self.length > 0:
            newNode.setNext(self.head)
        self.head = newNode

        self.length=self.length+1
        
    def partition(self, x):
        if self.head != None:
            current = self.head
            next = current.getNext()
            
            while next != None:
                
                if next.getData() < x:
                    
                    current.setNext(next.getNext())
                    next.setNext(self.head)
                    self.head = next
                    next = current.getNext()
                
                else:
                    current = current.getNext()
                    next = current.getNext()

    def __str__(self):
        if self.length==0:
            return "empty"
        else:
            l = ""
            current=self.head
            
            while current!=None:
                l+=str(current.getData()) + "-->"
                current = current.getNext()
            return l    

m=Element()
m.insert(10)
m.insert(50)
m.insert(30)
m.insert(40)
m.insert(78)
m.insert(20)
m.insert(58)
print m
m.partition(35)
print m
