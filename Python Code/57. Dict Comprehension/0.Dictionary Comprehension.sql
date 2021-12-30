#                                      Dictionary Comprehension


Dictionary comprehension represents creation of new Dictionary from an iterable object that satisfy a given condition.
Syntax:- 
new_dict = {expression(variable):expression(variable) for variable,variable in iterable_object if_statement}
There can be zero or more If Statements.
There can be one or multiple for loops. 
Ex:- 
dict1 = {k:v for k, v in lst}
dict2 = {n:n*2 for n in range(10)}
dict3 = {n:n*2 for n in range(20) if n%2==0}
dict4 = {n:n*2 for n in range(20) if n%2==0 if n%3==0}



Comprehension with If else Statement
Syntax:- 
new_dict = {expression(variable): (expression if_statement else expression) for variable in iterable_object}

Ex:-
new_dict = {i :(“even” if i%2==0 else “Invalid” for i in range(10)}
