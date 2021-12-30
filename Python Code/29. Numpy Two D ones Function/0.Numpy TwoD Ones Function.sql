#                                        ones( ) Function


ones ( ) Function is used to create 2D array with several rows and columns with all 1s.
Syntax:- 
numpy.ones(shape, dtype=float, order='C')
Where,
shape – shape of new array. It can be an int which will represent number of elements or can be tuple of int. ex:- (3, 2)

dtype – The desired data-type for the array. Default is float.

Order  - Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory. It can be C or F.




#                                      Creating 2D Array using ones ( ) Function


Syntax:- 
from numpy import *
array_name = ones(shape, dtype=float)
Ex:-
from numpy import *
a = ones((3, 2))



a = array([   [1., 1.],
	          [1., 1.],
              [1., 1.]   ])


1.              1.             1.              1.                1.              1.
a[0][0]       a[0][1]       a[1][0]        a[1][1]          a[2][0]           a[2][1]



#                                       Accessing 2D Array Elements


from numpy import *
a = ones((3, 2))
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])



a = array([   [1., 1.],
	          [1., 1.],
              [1., 1.]   ])



#                                           Accessing 2D Array using for loop


from numpy import *
a = ones((3, 2))

a = array([   [1., 1.],
	          [1., 1.],
              [1., 1.]   ])



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



#                                     Accessing 2D Array using while loop


from numpy import *
a = ones((3, 2))
n = len(a)
i = 0
while i < n :
         j = 0
         while j < len(a[i]):
	       print(a[i][j])
	       j+=1
         i+=1


a = ones((3, 2))


a = array([   [1., 1.],
	          [1., 1.],
              [1., 1.]   ])


