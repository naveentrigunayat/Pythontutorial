#                                         Operators

An operator is a symbol that performs an operation.
Arithmetic Operators
Relational Operators / Comparison Operators
Logical Operators 
Assignment Operators
Bitwise Operators
Membership Operators
Identity Operators


#                              Arithmetic Operators

Arithmetic Operators are used to perform basic arithmetic operations like addition, subtraction, division etc.


Operators              Meaning                                                               Example                           Result


+                     Addition                                                               4 + 2                               6
–                    Subtraction                                                             4 - 2                               2
*                    Multiplication                                                          4 * 2                               8
/                    Division                                                                4 / 2                               2  
%                    Modulus operator to get remainder in integer division                   5 % 2                               1  
**                   Exponent                                                                5 ** 2                              25
//                   Integer Division/ Floor Division                                        5 // 2                              2
                                                                                             -5 // 2                             -3



#                                          Relational/ Comparison Operators


Relational operators are used to compare the value of operands (expressions) to produce a logical value.
 A logical value is either True or False


 Operators              Meaning                                        Example                           Result

 <                     Less Than                                        5 < 2                             False
 >                     Greater Than                                     5 > 2                             True
 <=                    Less than or Equall To                           5 <= 2                            False
 >=                    Greater than or Equal To                         5 >= 2                            True 
 ==                    Equal to                                         5 == 2                            False
 !=                    Not Equal to                                     5 != 2                            True




 #                                       Logical Operators


 Logical operators are used to connect more relational operations to form a complex expression called logical expression.
  A value obtained by evaluating a logical expression is always logical, i.e. either True or False.
   

 Operators              Meaning                                      Example                      Result


and                Logical and                                     (5<2) and (5>3)                  False
or                 Logical or                                      (5<2) or (5>3)                   True
not                Logical not                                     not (5<2)                        True 



#                                   and


Operand 1                     Operand 2                   Result


True                          True                     True
True                         False                     False
False                        True                      False
False                        False                     False
True                         Expression                Expression
False                        Expression                False


True and Expression1 and Expression2 = Expression2
False and Expression1 and Expression2 = False



#                                    or

Operand 1                   Operand 2                   Result

True                        True                        True 
True                        False                       True
False                       True                        True
False                       False                       False
True                        Expression                  True
False                       Expression                  Expression



True or Expression1 or Expression2 = True
False or Expression1 or Expression2 = Expression1



#                                  not

Operand                 Result

False                   True
True                    False



#                               Assignment Operators

Assignment operators are used to perform arithmetic operations while assigning a value to a variable.


Operator             Example           Equivalent Expression (m=15)          Result

=                  y = a+b                 y = 10 + 20                          30
+=                 m +=10                  m = m+10                             25
-=                 m -=10                  m = m-10                             5
*=                 m *=10                  m = m*10                            150
/=                 m /=10                  m = m/10                            1.5
%=                 m %=10                  m = m%10                            5
**=                m**=2                   m = m**2 or 𝑚= 𝑚^2                 225
//=                m//=10                  m = m//10                           1



#                              Membership Operators


The membership operators are useful to test for membership in a sequence such as string, lists, tuples and dictionaries. 
There are two type of Membership operator:-
in 
not in


#                             in 


This operators is used to find an element in the specified sequence. 
It returns True if element is found in the specified sequence else it returns False.
Ex:- 
st1 = “Welcome to geekyshows”
“to” in st1             <-----  True

st2 = “Welcome top geekyshows”
“to” in st2                 <-----  True

st3 = “Welcome to geekyshows”
“subs” in st3                <-----  False


#                                   NOt In

This operators works in reverse manner for in operator. 
It returns True if element is not found in the specified sequence and if element is found, then it returns False.
Ex:- 
st1 = “Welcome to geekyshows”
“subs” not in st1           <-----  True

st2 = “Welcome to geekyshows”
“to” not in st2              <-----  False

st3 = “Welcome top geekyshows”
“to” not in st3               <-----  False



#                          Identity Operators


The identity operators compare the memory locations of two objects. Hence, it is possible to know whether two objects are same or not. 
There are two types of Identity operator:-
is 
is not


#                              is

This operator is used to compare whether two objects are same or not.  
It returns True if memory location of two objects are same else it returns False.


Ex:- 
a = 10
b = 10

a is b     <-----  True

a = 10
b = ‘10’

a is b       <------ False



#                                     is not 


This operator works in reverse manner for is operator. 
It returns True if memory location of two objects are not same and if they are same it returns False.
Ex:- 
a = 10
b = 10


a is not b    <------ False


a = 10
b = ‘10’

a is not b    <----- True


#                                   Operator Precedence and Associativity



The computer scans an expression which contains the operators from left to right and performs only one operation at a time. 
The expression will be scanned many times to produce the result. 
The order in which various operations are performed is known as hierarchy of operations or operator precedence. 
Some of the operators of the same level of precedence are evaluated from left to right or right to left. 
This is referred to associativity.



Order            Operator                                                 Meaning

1                    ( )                                                Parentheses

2                  **                                                   Exponentiation

3                  +, -, ~                                             Unary Plus, Unary Minus, Bitwise Not

4                 *, /, //, %                                          Multiplication, Division, Floor Division, Modulus

5                 +, -                                                 Addition, Subtraction

6                  <<, >>                                              Bitwise Left Shift, Bitwise Right Shift

7                  &                                                   Bitwise AND

8                   ^                                                  Bitwise XOR

9                  >, >=, <, <=, ==, !=                                Relational Operators

10                 =, %=, /=, //=, -=, +=, *=, **=                     Assignment Operators

11                 is, is not                                           Identity Operators

12                 in, not in                                          Membership Operators

13                 not                                                 Logical NOT

14                 or                                                  Logical OR

15                 and                                                 Logical AND




value = (1+1)*2**4//3+4-1                                        Parentheses
	2*2**4//3+4-1                                                 Exponentiation
	2*16//3+4-1                                                 Multiplication, Division, Modulus and Floor Division
	32//3+4-1                                                   
	10+4-1                                                         Addition and Subtraction
	14-1                                                           
	13                                                             Assignment






#                                            Bitwise Operators


Bitwise operators are used to perform operations at binary digit level. 
These operators are not commonly used and are used only in special applications where optimized use of storage is required.


Operator                              Meaning


&                                 Bitwise AND
|                                 Bitwise OR
^                                 Bitwise exclusive OR / Bitwise XOR
~                                 Bitwise inversion (one’s complement)
<<                                Shifts the bits to left / Bitwise Left Shift
>>                                Shifts the bits to right / Bitwise Right Shift



#                                         Bitwise AND &


Operand 1                    Operand 2                     Result (operand1 & operand2)

True 1                        True 1                        True 1

True 1                         False 0                       False 0

False 0                       True 1                          False 0

False 0                         False 0                     False 0


a = 10              0 0 0 0   1 0 1 0

b = 15              0 0 0 0   1 1 1 1



#                                        Bitwise OR |



Operand 1                    Operand 2                     Result (operand1 & operand2)

True 1                        True 1                        True 1

True 1                         False 0                       True 1

False 0                       True 1                          True 1

False 0                         False 0                     False 0



a = 10               0 0 0 0   1 0 1 0

b = 15               0 0 0 0   1 1 1 1


#                                        Bitwise XOR ^



Operand 1                    Operand 2                     Result (operand1 & operand2)

True 1                        True 1                        False 0

True 1                         False 0                       True 1

False 0                       True 1                          True 1

False 0                         False 0                     False 0



a = 10               0 0 0 0   1 0 1 0

b = 15               0 0 0 0   1 1 1 1



#                                          Bitwise NOT ~


Operand                       Result (~ operand)

True 1                     False 0

False 0                     True 1


a = 10               0 0 0 0   1 0 1 0


#                                 Bitwise Left Shift <<


                           a = 10 

                     0 0 0 0  1 0 1 0

                0 0 1 0  1 0 0 0     

                     a << 2


#                                 Bitwise Right Shift >>


                              a = 10

                      0 0 0 0  1 0 1 0
                       
                           0 0 0 0  0 0 1 0


                           a >> 2



