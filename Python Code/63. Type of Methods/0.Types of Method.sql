#                                            Type of Methods


1.Instance Methods  : 1> Accessor Methods  2> Mutator Methods

2.Class Methods

3.Static Methods


Instance methods are the methods which act upon the instance variables of the class.
Instance method need to know the memory address of the instance 
which is provided through self variable by default as first parameter for the instance method.


Syntax:- 
def method_name(self):                               <---------------  Instance Method without Parameter/Formal Arguments
	function body

def method_name(self, f1, f2):                      <----------------- Instance Method with Parameter/Formal Arguments
	function body



#                                      Instance Method without Parameter


class Mobile:

    def show_model(self):                              <------------  Instance Method
            print(“RealMe X”)

realme = Mobile( )



class Mobile:
     def __init__(self):
            self.model = ‘RealMe X’                      <-----------------   Instance variable

    def show_model(self):                               <-----------  Instance Method
            print(self.model)            <----------   Accessing Instance variable Inside Instance Method 


realme = Mobile( )



#                                 Calling Instance Method w/o Argument


Instance methods are bound to object of the class so we call instance method with object name.
Syntax:- object_name.method_name()


Ex:- realme.show_model()

class Mobile:
    def show_model(self):
            print(“RealMe X”)

realme = Mobile( )
realme.show_model()                     <---------------   Calling Instance Method w/o Argument



#                                       Instance Method with Parameter


class Mobile:
     def __init__(self):
            self.model = ‘RealMe X’                 <------  Instance variable

    def show_model(self, p):                        <---------   Instance Method with parameter
            self.price = p                   <------    Parameter             And            Instance Variable
            print(self.model, self.price)

realme = Mobile( )



#                           Calling Instance Method with Argument


Syntax:- object_name.method_name(Actual_argument)
Ex:- realme.show_model(1000)
class Mobile:
     def __init__(self):
            self.model = ‘RealMe X’
    def show_model(self, p):
            self.price = p
            print(self.model, self.price)

realme = Mobile( )
realme.show_model(1000)                         <-----------   Calling Method with argument




#                                     Accessor Method



This method is used to access or read data of the variables. This method do not modify the data in the variable. 
This is also called as getter method.


Ex:-
def get_value(self):
def get_result(self):
def get_name(self):
def get_id(self):



class Mobile:
    def __init__(self):
           self.model = ‘RealMe X’

    def get_model(self):
            return self.model

realme = Mobile( )
m = realme.get_model()
print(m)



#                                     Mutator Method



This method is used to access or read and modify data of the variables. This method modify the data in the variable. 
This is also called as setter method.


Ex:-
def set_value(self):
def set_result(self):
def set_name(self):
def set_id(self):



class Mobile:
    def __init__(self):
           self.model = ‘RealMe X’

    def set_model(self):
            self.model = ‘RealMe 2’

realme = Mobile( )
realme.set_model()



class Mobile:

    def set_model(self, m):
            self.model = m

realme = Mobile( )
realme.set_model(‘RealMe X’)




#                                        Class Methods


Class methods are the methods which act upon the class variables or static variable of the class.
Decorator @classmethod need to write above the class method.
By default, the first parameter of class method is cls which refers to the class itself.
Syntax:- 
@classmethod                     <------- Decorator
def method_name(cls):      <-------  Class Method without Parameter/Formal Arguments
	method body

@classmethod                      <-------    Decorator
def method_name(cls, f1, f2):              <------  Class Method with Parameter/Formal Arguments
	method body



#                            Class Method without Parameter


class Mobile:
    @classmethod                  <------  Decorator
    def show_model(cls):                 <-----  Class Method
            print(“RealMe X”)

realme = Mobile( )



class Mobile:
     fp = ‘Yes’               <------  Class Variable
    @classmethod                  <------  Decorator
    def show_model(cls):             <-----  Class Method
            print(cls.fp)      <---------   Accessing Class variable Inside Class Method 


realme = Mobile( )



#                                   Calling Class Method without Argument


Syntax:- Classname.method_name()

class Mobile:
    @classmethod
    def show_model(cls):
            print(“RealMe X”)

realme = Mobile( )
Mobile.show_model()                <---------   Calling Class Method w/o Argument




#                                  Class Method with Parameter



class Mobile:
     fp = ‘Yes’                       <----------   Class Variable
     @classmethod       <--------------  Decorator
    def show_model(cls, r):              <-------------   Defining Method with parameter
            cls.ram = r
            print(cls.fp, cls.ram)

realme = Mobile( )




#                                 Calling Class Method with Argument


Syntax:- Classname.method_name(Actual_argument)


Ex:- Mobile.show_model(‘4GB’)
class Mobile:
     fp = ‘Yes’
     @classmethod
     def show_model(cls, r):
            cls.ram = r
            print(cls.fp, cls.ram)

realme = Mobile( )
Mobile.show_model(101)             <---------   Calling Method with argument




#                                 Static Methods



Static Methods are used when some processing is related to the class but does not need the class or its instances to perform any work. 
We use static method when we want to pass some values from outside and perform some action in the method.
Decorator @staticmethod need to write above the static method.
Syntax:- 
@staticmethod                 <------  Decorator
def method_name():              <------|  Static Method without Parameter/Formal Arguments
	method body             <------|  Static Method without Parameter/Formal Arguments



@staticmethod
def method_name(f1, f2):
	method body



#                               Static Method without Parameter



class Mobile:
    @staticmethod                   <--------  Decorator
    def show_model():             <----------   Static Method
            print(“RealMe X”)

realme = Mobile( )



class Mobile:
     fp = ‘Yes’
    @staticmethod               <----------  Static Method
    def show_model():
            print(Mobile.fp)

realme = Mobile( )




#                                  Calling Static Method without Argument


Syntax:- Classname.method_name()

class Mobile:
    @staticmethod
    def show_model():
            print(“RealMe X”)

realme = Mobile( )
Mobile.show_model()               <-----------    Calling Static Method w/o Argument



#                                Static Method with Parameter


class Mobile:
     @staticmethod              <--------  Decorator
    def show_model(m, p):             <-------  Defining Method with parameter
            model = m
            price = p
            print(model, price)
realme = Mobile( )



#                             Calling Static Method with Argument


Syntax:- Classname.method_name(Actual_argument)


Ex:- Mobile.show_model(1000)
class Mobile:
     @staticmethod
    def show_model(m, p):
            model = m
            price = p
            print(model, price)
realme = Mobile( )
Mobile.show_model(‘RealMe X’, 1000)            <--------   Calling Method with argument


