#                                  linspace ( ) Function

linspace ( ) Function is used to create an array with evenly spaced numbers between a start point and stop point.
Syntax:- 
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
Where,
start – It represents starting element.
stop – It represents ending element.
num – It represents number of parts the element should be divided. Default is 50. It must be non-negative.
endpoint- If True, stop is the last element. If False, stop is not included.

https://www.numpy.org/devdocs/reference/generated/numpy.linspace.html


#                                  Creating Array using linspace ( ) Function


Syntax:- 
from numpy import *
array_name = linspace(start, stop, num=50, endpoint=True)

Ex:-
from numpy import *
a = linspace(1, 8)
a = linspace(1, 8, num=5)
a = linspace(1, 8, 5)
a = linspace(1, 8, 5, endpoint=False)



#                                 Accessing One-D Array Elements


from numpy import *
a = linspace(1, 8, 5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])



#                                Accessing using for loop


from numpy import *
a = linspace(1, 8, 5)

Without index
for el in a:
	print(el)

With index
n = len(a)
for i in range(n):
	print(a[i])



#                                    Accessing using while loop

from numpy import *
a = linspace(1, 8, 5)

n = len(a)
i = 0
while i < n :
	print(a[i])
	i+=1
