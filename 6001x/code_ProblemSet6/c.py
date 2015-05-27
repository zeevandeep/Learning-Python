class En(object):
		
	def encrypt(k):
		plaintext = input('Enter plain text message: ')
		cipher = ''
	
		for each in plaintext:
			c = (ord(each)+k) % 126
			print( ord(each))
		
			if c < 32: 
				c+=31
			
			cipher += chr(c)
		
		print ('Your encrypted message is: ' + cipher)
