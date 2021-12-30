#                                             pip


pip is the package manager for Python. Using pip we can install python packages.


How to Install pip
pip is distributed with Python which means that when you download Python from https://www.python.org/ , you automatically get pip installed on your computer.

Check if pip is already Installed
pip --version

Update pip
python -m pip install --upgrade pip
py -m pip install --upgrade pip 


How to Get Help
pip help – It shows list of pip commands and their functions.

How to install Packages
pip install camelcase

How to Use Packages
import camelcase

How to Uninstall Packages
pip uninstall camelcase


#                                       numpy

In Python, Numpy is a package which contains classes, functions, variables, large library of mathematical functions etc to work with scientific calculation.
Numpy can be used to create n dimensional arrays where n is any integer. We can create 1 dimensional array, 2 dimensional array, 3 dimensional array and so on.
Numpy’s array class is called ndarray. It is also known by alias name array. There is another class array in python which is different from numpy’s array class. 



#                                              Import numpy


There are two ways to import numpy:-
import numpy – This will import the entire numpy module.

from numpy import * - This will import all class, objects, variable etc from numpy package. Here * means All. 


#                                        One Dimensional Array

Single Row Multiple Columns
Ex:- [101, 102, 103, 104, 105]



#                                          Ways of Creating Array in numpy

array ( ) Function
linspace ( ) Function
logspace ( ) Function
arange ( ) Function
zeros ( ) Function
ones ( ) Function


#                                            array ( ) Function


array ( ) Function of numpy module is used to create an array.
Syntax:- 
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

https://www.numpy.org/devdocs/reference/generated/numpy.array.html



#                                Creating 1D Array using array ( ) Function


Syntax:-                 array Function
import numpy             /
array_name = numpy.array([elements])

Ex:-
import numpy
stu_roll = numpy.array([101, 102, 103, 104, 105])
stu_roll = numpy.array([101, 102, 103, 104, 105], int)
a = numpy.array([10.1, 5.2, 4.23, 10.4, 1.5], float)
a = numpy.array([10.1, 5.2, 4.23, 10.4, 1.5])
ar = numpy.array([‘a’, ‘b’, ‘c’, ‘d’])
name = numpy.array([‘Rahul’, ‘Sonam’, ‘Raj’], dtype=str)
name = numpy.array([‘Rahul’, ‘Sonam’, ‘Raj’])



#                                  Creating 1D Array using array ( ) Function


Syntax:- 
from numpy import *
array_name = array([elements])

Ex:- 
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])



#                                        index


An index represents the position number of an array’s element.
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])



 [101,                    102,           103,                104,               105]

 0                          1             2                   3                  4



#                                    Accessing One-D Array Elements


from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])


                             

                             [101,                    102,           103,                104,               105]


                             stu_roll[0]         stu_roll[1]      stu_roll[2]    stu_roll[3]          stu_roll[4]



 
#                                  Modifying 1D Array Elements


from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
stu_roll[1] = 110
print(stu_roll[1])



                             [101,                    102,           103,                104,               105]


                             stu_roll[0]         stu_roll[1]      stu_roll[2]    stu_roll[3]          stu_roll[4]




#                               Accessing array using for loop


from numpy import *
stu_roll = array([101, 102, 103, 104, 105])

Without index
for element in stu_roll:
	print(element)

With index
n = len(stu_roll)
for i in range(n):
	print(stu_roll[i])



#                                  Accessing array using while loop


from numpy import *
stu_roll = array([101, 102, 103, 104, 105])

n = len(stu_roll)
i = 0
while i < n :
	print(stu_roll[i])
	i+=1



