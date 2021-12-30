#                                          Constructor


Python supports a special type of method called constructor for initializing the instance variable of a class. 
A class constructor, if defined is called whenever a program creates an object of that class. 
A constructor is called only once at the time of creating an instance.
If two instances are created for a class, the constructor will be called once for each instance.  



#                            Constructor without Parameter


class Mobile:
     def __init__(self):
          self.model =‘RealMe X’

realme = Mobile( )



#                              Constructor with Parameter


class Mobile:
     def __init__(self, m):
          self.model = m
realme = Mobile('Realme X')

class Mobile:
def __init__(self, m, v=80):
       self.model = m
       self.volumn = v
redmi = Mobile('Redmi 7s', 50)
