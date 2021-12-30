#                                          Comprehension


Comprehension contains very compact code usually a single statement that perform a task.
List Comprehension
Set Comprehension
Dictionary Comprehension



#                                    List Comprehension


List comprehension represents creation of new list from an iterable object that satisfy a given condition.
Syntax:- 
new_list = [expression for item in iterable_object if_statement]
There can be zero or more If Statements.
There can be one or multiple for loops. 
Ex:- 
lst1 = [i+1 for i in range(20)]
lst2 = [i for i in range(20) if i%2==0]
lst3 = [i for i in range(11) if i%2==0 if i%3==0]            <---- Nested If statement



#                                    List Comprehension

List Comprehension with If else Statement
Syntax:- 
new_list = [expression if_statement else expression for item in iterable_object]
Ex:-
new_list = [i if i%2==0 else “Invalid” for i in range(10)]


#                        Nested List Comprehension


lst =[ [i*j for j in range(4,7)] for i in range(6,8) ]
             /                        \
     Inner for loop                  Outer for loop


