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
		self.head1=None
		self.length1=0


	def insert(self,data):
		newNode=Node()
		newNode.setData(data)


		if self.length > 0:
			newNode.setNext(self.head)
		self.head = newNode

		self.length+=1

	
	def __str__(self):
		if self.length==0:
			return "empty"
		else:
			l = ""
			current=self.head
			
			while current!=None:
				l+=str(current.getData()) + "-->"
				current = current.getNext()
		if self.length1==0:
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

	def SecondLinkLikstAtLast(self,data):
		secondNode=Node()
		secondNode.setData(data)

		if self.length1==0:
			self.head1=secondNode
		else:
			current=self.head1
			while current.getNext()!=None:
				current=current.getNext()
			current.setNext(secondNode)
		self.length1+=1


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

	def addTwoNuminLinkList(self, otherList):
		current=self.head
		current1=otherList.head
		l=""
		j=""
		
		while current != None:
			l+=str(current.getData())
			current=current.getNext()
		
		while  current1 != None:
			j+=str(current1.getData())
			current1=current1.getNext()
		result = str (int(l[::-1])+ int(j[::-1]))
		#print result
		
		resultList = list()
		for c in result:
			resultList.insert(int(c))

		return resultList

	def addTwoNuminLinkListEachNodeAtTime(self, otherList):
		current=self.head
		current1=otherList.head
		l=""
		j=""
		
		while current1!=None or current=None:
			
			l=current.getData()
			j=current1.getData()
			while current != None:
				l=current.getData()
			current=current.getNext()
		
		while  current1 != None:
			j+=str(current1.getData())
			current1=current1.getNext()
		result = str (int(l[::-1])+ int(j[::-1]))
		#print result
		
		resultList = list()
		for c in result:
			resultList.insert(int(c))

		return resultList
			









	


if __name__ == "__main__":
	m=list()
	m.insertLast(7)
	m.insertLast(1)
	m.insertLast(6)
	
	n = list()
	n.insertLast(5)
	n.insertLast(9)
	n.insertLast(2)
	
	print m.addTwoNuminLinkList(n)
	
	





