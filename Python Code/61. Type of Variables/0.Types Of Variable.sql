#                                                Type of Variable


Instance Variable 
Class Variable / Static Variable


#                                        Instance Variable 

Instance variables are the variables whose separate copy is created in every object.
Instance variables are defined and initialized using a constructor with self parameter. 
Ex:-
class Mobile:
     def __init__(self):
	    self.model = ‘RealMe X’                           <------- Instance Variable
    def show_model(self):
	    print(self.model)
realme = Mobile( )


#                                       Accessing Instance Variable 


1. With Instance Method :

To access instance variable, we need instance methods with self as first parameter then we can access instance variable using 
self.variable_name


class Mobile:
     def __init__(self):
	    self.model = ‘RealMe X’                 <-------------     Instance Variable
    def show_model(self):                     <-------------- Instance Method
	    self.model                         <---------  Accessing Instance Variable 
realme = Mobile( )


2. Outside Class
We can access instance variable using object_name.variable_name


class Mobile:
     def __init__(self):
	    self.model = ‘RealMe X’                  <-------------     Instance Variable
    def show_model(self):                  <-------------- Instance Method
	    self.model                 <---------  Accessing Instance Variable 

realme = Mobile( )
realme.model                       <----------- Accessing Instance Variable from outside Class




#                                          'Instance Variable'


Instance variables are the variables whose separate copy is created in every object.
If we modify the copy of Instance variable in an instance, it will not effect all the copies in the other instance. 



class Mobile:
     def __init__(self):
	    self.model = ‘RealMe X’                    <-------------     Instance Variable
    def show_model(self):
	    print(self.model)
realme = Mobile( )
redmi = Mobile( )
geek = Mobile( )





#                                  Heap Memory


#                             self.model = ‘RealMe X
                                      realme

                             
#                              self.model = ‘RealMe X
                                     redmi


#                              self.model = ‘RealMe X
                                      geek






#                               'Class Variable / Static Variable'


Class variables are the variables whose single copy is available to all the instance of the class. 
If we modify the copy of class variable in an instance, it will effect all the copies in the other instance. 


Ex:- 
class Mobile:
     fp = ‘Yes’                                    <---------------  Class Variable
     def __init__(self):
           self.model = ‘RealMe X’

    def show_model(self):
          print(self.model)

realme = Mobile( )


#                                   'Accessing Class/Static Variable '


1. With Class Method :
To access class variable, we need class methods with cls as first parameter then we can access class variable using cls.variable_name


class Mobile:
     fp = ‘Yes’                                                  <---------------  Class Variable
     def __init__(self):
           self.model = ‘RealMe X’
    def show_model(self):
          print(self.model)
     @classmethod                                <----------------------------   Class Method
     def is_fp(cls):
           cls.fp                             <-----------------------------  Accessing Class Variable inside Class Method

realme = Mobile( )


2. Outside Class
We can access class variable using Classname.variable_name


class Mobile:
     fp = ‘Yes’                      <---------------  Class Variable

     @classmethod                               <----------------------------   Class Method
     def show(cls):
           cls.fp                                          <-----------------------------  Accessing Class Variable inside Class Method

realme = Mobile( )

Mobile.fp                                  <------------------------   Accessing Class Variable outside class





#                                        'Class Variable / Static Variable'


Class variables are the variables whose single copy is available to all the instance of the class. 
If we modify the copy of class variable in an instance, it will effect all the copies in the other instance. 



class Mobile:
     fp = ‘Yes’
     @classmethod
     def is_fp(cls):
           print(cls.fp)
realme = Mobile( )
redmi = Mobile( )
geek = Mobile( )
print(Mobile.fp)



'''                                    Heap Memory


                                     fp = ‘Yes’
                                     /   |    \
                                    /    |     \
                                   /     |      \
                                  /      |       \
                                 /       |        \
                            realme     redmi     geek

'''


