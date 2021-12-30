#                                    arange( ) Function


arange ( ) Function is used to create an array with a group of elements from start to one element prior to stop in steps of stepsize.
Syntax:- 
numpy.arange(start, stop, stepsize, dtype=None)
Where,
start – Start of interval. The interval includes this value. The default start value is 0.
stop – End of interval. The interval does not include this value, except in some cases where step is not an integer and floating point round-off affects the length of out.
stepsize – Spacing between values. The default step size is 1. 
dtype – The type of output array.



#                          Creating Array using arange ( ) Function


Syntax:- 
from numpy import *
array_name = arange(start, stop, stepsize, dtype=None)

Ex:-
from numpy import *
a = arange(5)
a = arange(5.0)
a = arange(1, 6)
a = arange(1, 10, 2,)


0.0         1.0         2.0         3.0        4.0
a[0]       a[1]         a[2]        a[3]       a[4]


#                             Accessing One-D Array Elements


from numpy import *
a = arange(5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])



#                             Accessing using for loop


from numpy import *
a = arange(5)

Without index
for el in a:
	print(el)

With index
n = len(a)
for i in range(n):
	print(a[i])



#                              Accessing using while loop


from numpy import *
a = arange(5)

n = len(a)
i = 0
while i < n :
	print(a[i])
	i+=1



