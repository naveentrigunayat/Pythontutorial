#                                     Set Comprehension


Set comprehension represents creation of new set from an iterable object that satisfy a given condition.
Syntax:- 
new_set = {expression for item in iterable_object if_statement}
There can be zero or more If Statements.
There can be one or multiple for loops. 
Ex:- 
set1 = {i+1 for i in range(20)}
set2 = {i for i in range(20) if i%2==0}
set3 = {i for i in range(11) if i%2==0 if i%3==0}



Set Comprehension with If else Statement
Syntax:- 
new_set= {expression if_statement else expression for item in iterable_object}
Ex:-
new_set = {i if i%2==0 else i*1000 for i in range(10)}



#                                   Nested Set Comprehension


st = {(I, j) for j in range(4,7) for i in range(6,8)}
