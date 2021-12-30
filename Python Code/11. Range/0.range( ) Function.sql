#                                   range( ) Function


range() function is used to generate a sequence of integers starting from 0 by default, and increments by 1 by default, till j-1. 
Syntax:- 
range(start, stop, stepsize)
Start – Starting position. If we do not mention start by default it’s 0
*Stop – Ending position. The range of integers stops one element prior to stop. If stop is j then it will stop at exact j-1
Stepsize – Increment by stepsize. If we do not mention start by default it’s 1



Syntax:-  range( j )		0, 1, 2, 3, 4,………..., j-1
Ex:-  range(10)		0, 1, 2, 3, 4, 5, 6, 7, 8, 9

Syntax:- range(i, j)		i, i+1, i+2. i+3,….., j-1  
Ex:- range(1, 10)		1, 2, 3, 4, 5, 6, 7, 8, 9

Syntax: - range(i, j, k)	i, i+k, i+2k, i+3k, i+4k,….., j-1
range(1, 10, 2)		1, 3, 5, 7, 9

range(-1, -10, -2)	-1  -3  -5  -7  -9
range(10, 0, -1)	10  9  8  7  6  5  4  3  2  1



#                                            Rules:-


All argument must be integers, whether its positive or negative
You can not pass a string or float number or any other type in a start, stop and stepsize.
The stepsize value should not be zero.



