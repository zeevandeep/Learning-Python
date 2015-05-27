import numpy as np
class Loop:
	def __init__(self):
		self.data=None
		self.next=None
	def setdata(self,data):
		self.data=data
		return
	def getdata(self):
		return self.data
	def setnext(self,next):
		self.next=next
	def getnext(self):
		return self.next
	def length(self):
		return len(self)


class list1:
	def __init__(self,data,data1,data2,data3):
		newNode=Loop()
		newNode1=Loop()
		newNode2=Loop()
		newNode3=Loop()

		newNode.setdata(data)
		newNode1.setdata(data1)
		newNode2.setdata(data2)
		newNode3.setdata(data3)
		newNode.setnext(newNode1)
		newNode1.setnext(newNode2)
		newNode2.setnext(newNode3)
		newNode3.setnext(newNode1)
		self.length=1
		self.head=newNode

	def __str__(self):
		l=""
		current = self.head
		while current != None:
			l+= str(current.getdata())+ "--->"
			if self.length>5:
				break
			current=current.getnext()
			self.length+=1

		return l
	
	def Loop(self):
		current=self.head
		
		src=[]
		dest=[]
		i=0

		while True:


			src.append(id(current))
			dest.append(id(current.getnext()))
			
			if src[i-1] == dest[i]:
				print src
				print dest
				print ""
				print "Cycle found ", current.getdata(), current.getnext().getdata()
				break
			current=current.getnext()
			i=i+1





a=list1(2,3,4,5)
print a.Loop()




