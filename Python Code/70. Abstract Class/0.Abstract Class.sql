#                                      Abstract Class


A class derived from ABC class which belongs to abc module, is known as abstract class in Python. 
ABC Class is known as Meta Class which means a class that defines the behavior of other classes. 
So we can say, Meta Class ABC defines that the class which is derived from it becomes an abstract class.
Abstract Class can have abstract method and concrete methods. 
Abstract Class needs to be extended and its method implemented. 
PVM can not create objects of an abstract class.
Ex:-
from abc import ABC, abstractmethod
Class Father(ABC):


                                      
#                                         Abstract Method


A abstract method is a method whose action is redefined in the child classes as per the requirement of the object. 
We can declare a method as abstract method by using @abstractmethod decorator.
Ex:- 
from abc import ABC, abstractmethod
Class Father(ABC):
       @abstractmethod
        def disp(self):
                pass



#                                        Concrete Method


A Concrete method is a method whose action is defined in the abstract class itself. 
Ex:- 
from abc import ABC, abstractmethod
Class Father(ABC):
       @abstractmethod               
        def disp(self):              <---------             Abstract Method / Method Without Body
                pass
        def show(self):                   <------          Concrete Method / Method with Body
                print(“Concrete Method”)



#                                            Rules: 


PVM can not create objects of an abstract class. 
It is not necessary to declare all methods abstract in a abstract class.
Abstract Class can have abstract method and concrete methods. 
If there is any abstract method in a class, that class must be abstract.
The abstract methods of an abstract class must be defined in its child class/subclass.
If you are inheriting any abstract class that have abstract method, 
you must either provide the implementation of the method or make this class abstract


#                                        When use Abstract Class


We use abstract class when there are some common feature shared by all the objects as they are.
 


                                              Defence 
                                              Gun = AK 47 
                                              Area =  

                                                 |
                                                 |
                            -------------------- | --------------------
                            |                    |                     |
                            |                    |                     |
                            |                    |                     |
                            |                    |                     |

                        Army                   Air Force              Navy
                        Gun = AK 47            Gun = AK 47            Gun = AK 47
                        Area =Land             Area = Sky             Area = Sea

Gun is the common feature
shared by all Forces but area 
is different for them.


