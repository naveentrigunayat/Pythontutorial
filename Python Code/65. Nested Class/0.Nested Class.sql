#                                        Nested Class


A class within a class is called as nested class or nesting of a class.

class OuterClassName:
         def __init__(self):
               self.variable_name = value
               self.innerClassObjectName = self.InnerClassName( )                 <------ Inner Class Object
        def method_name(self):
               method body

         class InnerClassName:
               def __init__(self):
                      self.variable_name = value
               def method_name(self):
                      method body





class Army:                      <--------    Outer Class
       def __init__(self):
             self.name = ‘Rahul’
             self.gn = self.Gun()        <------   Inner Class Object
       def show(self):
             print(self.name)
       class Gun:                      <---------   Inner Class
             def __init__(self):
	self.name = ‘AK47’
	self.capacity = ’75 Rounds’
	self.length = ‘34.3 in’	
            def disp(self):
                  print(self.name, self.capacity, self.length)
                  
a = Army()           <-----   Outer Class Object

