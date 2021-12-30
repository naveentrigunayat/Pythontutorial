#                                      Multi-Dimensional Array


The 2D arrays, 3D arrays, etc are called Multi-dimensional Arrays. 



#                             Two Dimensional Array


If an array contains more than 1 row and 1 column that is known as Two Dimensional Array. It is also known as array of arrays.
Ex:- 
a = array([   [10, 20, 30, 40],
	     [50, 60, 70, 80]     ])
Similarly we can create 3D array.
Ex:- 
a = array ([  [  [2, 5, 8], [6, 4, 3]   ],   
	      [  [3, 7, 9], [5, 4, 9]  ]	])



#                                    Way of creating Multi-D Array


array ( ) Function
zeros ( ) Function
ones ( ) Function
reshape ( ) Function



#                                 array ( ) Function


array ( ) Function of numpy is used to create a multi dimensional array. 
Syntax:- 
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

https://www.numpy.org/devdocs/reference/generated/numpy.array.html



#                                     Creating 2D Array using array ( ) Function


Syntax:- 
import numpy
array_name = numpy.array([  [elements],  [elements]  ])

Ex:-
import numpy
a = numpy.array([   [10, 20, 30, 40],  [50, 60, 70, 80]     ])
a = numpy.array([   [10, 20, 30, 40],
	              [50, 60, 70, 80]     ])
a = numpy.array([   [‘Rahul’, ‘Sonam’, ‘Raj’],
	              [‘Dell’, ‘Asus’, ‘Lenovo’]     ], dtype=str)


#                                           Creating and Initializing 2D Array

Syntax:- 
from numpy import *
array_name = array([  [elements],  [elements]  ])

Ex:- 
from numpy import *
a = array([   [10, 20, 30, 40],
                    [50, 60, 70, 80]   ])



#                                              index


An index represents the position number of an array’s element.
from numpy import *
a = array([   [10, 20, 30, 40],
                    [50, 60, 70, 80]   ])


 10           20          30          40          50           60            70             80
[0][0]      [0][1]      [0][2]      [0][3]       [1][0]      [1][1]         [1][2]         [1][3]



#                                           Accessing 2D Array Elements


from numpy import *
a = array([   [10, 20, 30, 40],
                    [50, 60, 70, 80]   ])
print(a[0][0])
print(a[0] [1])
print(a[0] [2])
print(a[0] [3])
print(a[1] [0])
print(a[1] [1])
print(a[1] [2])
print(a[1] [3])



 10           20          30          40          50           60            70             80
[0][0]      [0][1]      [0][2]      [0][3]       [1][0]      [1][1]         [1][2]         [1][3]



#                                      Modifying 2D Array Elements


from numpy import *
a = array([   [10, 20, 30, 40],
                    [50, 60, 70, 80]   ])
a[1][2] = 100
print(a[1][2])



#                                     Accessing 2D Array using for loop


from numpy import *
a = array([   [10, 20, 30, 40],
                    [50, 60, 70, 80]   ])



Without index
for r in a:
       for c in r:
	print(c)
       print( )


--------------------



With index
n = len(a)
for i in range(n):
        for j in range(len(a[i])):
	print(a[i][j])
         print ( )



The outer for loop represents the rows and the inner for loop represents the columns in each row.



#                                 Accessing 2D Array using while loop


from numpy import *
a = array([   [10, 20, 30, 40],
                    [50, 60, 70, 80]   ])
n = len(a)
i = 0
while i < n :
         j = 0
         while j < len(a[i]):
	       print(a[i][j])
	       j+=1
         i+=1




