
'''                                               Constructor


Python supports a special type of method called constructor for initializing the instance variable of a class. 
A class constructor, if defined is called whenever a program creates an object of that class. 
A constructor is called only once at the time of creating an instance.
If two instances are created for a class, the constructor will be called once for each instance.  


'''

#                               Constructor with Parameter


# Constructor
class Mobile:
	# Constructor
	def __init__(self, m, v=80):
		self.model = m
		self.volumn = v
		
	def show_model(self, p):
		price = p				# Local Varaible
		print("Model:", self.model, "and Price:", price)
		print("Volumn:", self.volumn)

# Passing Argument to Constructor
realme = Mobile('Realme X')

# Accessing Method from outside Class
realme.show_model(1000)



