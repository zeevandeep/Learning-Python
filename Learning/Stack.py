class Stack():
	
	def __init__(self,limit=10):
		
		self.stk=[]
		self.minStk=[]
		self.limit=limit
	
	def push(self,data):
		
		if len(self.stk) > self.limit:
			self.resize() 	
		self.stk.append(data)
		if len(self.minStk)==0 or data<self.minStk[-1]:
			self.minStk.append(data)
		

	def pop(self):
		
		if len(self.stk)<=0:
			return 'Underflow'
		else:

			x = self.stk.pop()
		if x==self.minStk[-1]:
			self.minStk.pop()
		return self.stk.pop()


	def len(self):
		
		return len(self.stk)

	def peek(self):
		if len(self.stk)<=0:
			print "Stack Overflow!"
		else:
			return self.stk[-1]

	def resize(self):
		newStk=list(self.stk)
		self.limit=self.limit*2
		self.stk=newStk

	def CheckBalancingOfSymbols(self, input):
		
		d = {')' : '(', '}' : '{', ']' : '['}

		for symbols in input:
			print self.stk
			if symbols in ["{","[","("]:
				#print "push"
				self.push(symbols)
				
			
			elif len(self.stk)<=0:
				print "False len check"
				return False

			else:
				
				topSymbol=self.pop()
				

				if topSymbol == d[symbols]:
					continue	
				else:
					print "Not equal"
					return False
			#print "bal", bal

		return True
	def minimum(self):

		return self.minStk[-1]

	

a=Stack()
a.push(56)
a.push(86)
a.push(36)

a.push(6)
a.push(26)

a.push(7)
a.pop()
a.pop()
a.pop()
print a.minimum()









