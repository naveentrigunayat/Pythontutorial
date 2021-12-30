'''                            Accessing Class/Static Variable

Outside Class
We can access class variable using Classname.variable_name


'''

'''                               Class Variable / Static Variable

Class variables are the variables whose single copy is available to all the instance of the class. 
If we modify the copy of class variable in an instance, it will effect all the copies in the other instance. 


'''


# Accessing Class Variable from outside Class
class Mobile:
	fp = 'Yes'								# Class Variable
	
	def __init__(self):
		self.model = 'RealMe X'					# Instance Variable
	
	def show_model(self):						# Instance Method
		print("Model:",self.model)				# Accessing Instance Variable
		
	@classmethod								# Class Method
	def is_fp(cls):
		print("Finger Print:", cls.fp)		# Accessing Class Variable

		
realme = Mobile()
realme.show_model()
Mobile.is_fp()
print()
Mobile.fp = 'No'			# Accessing Class Variable from outside Class
Mobile.is_fp()



