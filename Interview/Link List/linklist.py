class Node:
	def __init__(self):
		self.data=None
		self.next=None
	
	def setData(self,data):
		self.data=data
	
	def getData(self):

		return self.data
	
	def setNext(self,next):
		self.next=next
	
	def getNext(self):
		return self.next
	
	def hasNext(self):
		return self.next!=None

	def __str__(self):
		return str(self.data)
	
	
	
class list:
	def __init__(self):
		self.head=None
		self.length=0


	def insert(self,data):
		newNode=Node()
		newNode.setData(data)


		if self.length > 0:
			newNode.setNext(self.head)
		self.head = newNode

		self.length+=1

	"""def print_list(newNode):
    	while newNode:
        	print newNode,
        	newNode = newNode.next
    	print"""
	
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

	def insertLast(self,data):
		newNode=Node()
		newNode.setData(data)

		if self.length==0:
			self.head=newNode
		else:
			current=self.head
			while current.getNext()!=None:
				current=current.getNext()
			current.setNext(newNode)
		self.length+=1

	def search(self,data):
		current=self.head
		while current!=None:
			if current.data == data:
				return True
			current=current.getNext()
		return False
	
	def deleteAtpos(self,pos):
		current=self.head
		previous=self.head
		count=1
		while count < pos-1:
			current=current.getNext()
			previous=previous.getNext()
			count+=1
		current=current.getNext()
		previous.setNext(current.getNext())
		return pos
		
	
	def deleteAtend(self):
		current=self.head
		previous=self.head
		while current.getNext()!=None:
			previous = current
			current=current.getNext()
		previous.setNext(None)
		return
	
	def removeDuplicates(self):
		current=self.head
		
		while current != None:
			next=current.getNext()
			previous=current
			#print "current ", current
			while next != None:
				#print "previous", previous
				#print "next", next
				if current.data == next.data:	
					previous.setNext(next.getNext())
					previous = previous.getNext()
					if previous == None or previous.getNext() == None:
						next = None
					elif previous.getNext() != None:
						next = previous.getNext()
					
				
			 	else:
			 		previous=next
			 		next=next.getNext()
		 	#print "List: ", self
		 	current = current.getNext()

	def reverse(self):
		print " "
		current=self.head
		l=""
		rcurrent=current.getNext()
		current.setNext(None)
		while rcurrent!=None:
			
			
			current1=rcurrent.getNext()
			rcurrent.setNext(current)
			current=rcurrent
			rcurrent=current1
		
		return current

	def Palindrome(self):
		current=self.head
		last=self.head
		b=0
		if last!=None:
			self.Palindrome(last.getNext())
		if current.getData() == last.getData():
			current=current.getNext()
			b=0
		else:
			b=1


		


		
		








	


if __name__ == "__main__":
	m=list()
	m.insertLast(1)
	m.insertLast(2)
	m.insertLast(3)
	m.insertLast(4)
	m.insertLast(4)
	m.insertLast(3)
	m.insertLast(2)
	m.insertLast(1)
	print m
	print m.Palindrome()
	







