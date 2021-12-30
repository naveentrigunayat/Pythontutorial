#                                        Relational/ Comparison Operators



Relational operators are used to compare the value of operands (expressions) to produce a logical value. A logical value is either True or False.


 Operators              Meaning                                        Example                           Result

 <                     Less Than                                        5 < 2                             False
 >                     Greater Than                                     5 > 2                             True
 <=                    Less than or Equall To                           5 <= 2                            False
 >=                    Greater than or Equal To                         5 >= 2                            True 
 ==                    Equal to                                         5 == 2                            False
 !=                    Not Equal to                                     5 != 2                            True



#                                  Comparing Arrays using numpy


Comparison operators can be used to compare arrays. The size of array must be same. Comparison operators compares the corresponding elements of the arrays and returns another array with Boolean value. 
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
c = a == b



any ( ) Function – This function returns True, if any one element of the iterable is True. If iterable is empty then returns False.
	Ex:- 
	a = array([100, 200, 300, 400, 500])
	b = array([100, 20, 30, 400, 50])
	c = a == b
	any(c)

all ( ) Function – This function returns True, if all element of the iterable are True or iterable is empty.
	Ex:- 
	a = array([100, 200, 300, 400, 500])
	b = array([100, 200, 300, 400, 500])
	c = a == b
	all(c)


Note - These are python’s built-in Functions


where ( ) Function- This function is used to create a new Array which contains, returned element chosen from expression1 or expression2 depending on condition. If condition is True expression1 is executed else expression 2. 
	Syntax:- numpy.where(condition, expression1, expression2)
	Ex:-
	a = array([100, 200, 300, 400, 500])
	b = array([10, 201, 30, 40, 50])
	c = where(a>b, a, b)


nonzero ( ) Function- This function is used to determine the positions of elements which are non zero. This function returns an array that contains the indexes of the element of the array which are not equal to zero
	Syntax:- numpy.nonzero(a)
	Ex:-
	a = array([100, 200, 300, 400, 500])
	c = nonzero(a)
