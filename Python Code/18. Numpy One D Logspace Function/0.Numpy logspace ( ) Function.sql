#                                         logspace ( ) Function

logspace ( ) Function is used to create an array with evenly spaced numbers logarithmically. The sequence starts at base ** start (base to the power of start) and ends with base ** stop.
Syntax:- 
numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
Where,
start – It represents starting element which will become base to the power of start 〖(𝑏𝑎𝑠𝑒〗^𝑠𝑡𝑎𝑟𝑡)
stop – It represents ending element which will become base to the power of stop (〖𝑏𝑎𝑠𝑒〗^𝑠𝑡𝑜𝑝)
num – It represents number of parts the element should be divided. Default is 50. It must be non-negative.
endpoint- If True, stop is the last element. If False, stop is not included.
base - The base of the log space.
dtype – The type of output array.



#                                      Creating Array using logspace ( ) Function


Syntax:- 
from numpy import *
array_name = logspace(start, stop, num=50, endpoint=True, base=10.0 dtype=None)


         10^1  10^3
Ex:-         \  |
a = logspace(1, 3)

from numpy import *
a = logspace(1, 3)
a = logspace(1, 3, 5)
a = logspace(1, 3, 5, base=12.0)


10.0        31.62       100.0       316.2     1000.0
a[0]        a[1]        a[2]        a[3]      a[4]



#                                         Accessing One-D Array Elements


from numpy import *
a = logspace(1, 3, 5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])



10.0        31.62       100.0       316.2     1000.0
a[0]        a[1]        a[2]        a[3]      a[4]



#                                             Accessing using for loop


from numpy import *
a = logspace(1, 3, 5)

Without index
for el in a:
	print(el)

With index
n = len(a)
for i in range(n):
	print(a[i])



#                                   Accessing using while loop


from numpy import *
a = logspace(1, 3, 5)

n = len(a)
i = 0
while i < n :
	print(a[i])
	i+=1



