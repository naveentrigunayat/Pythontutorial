#                               id ( ) Function


This function returns the “identity” of an object. 
The identity number is an integer which is guaranteed to be unique and constant for this object during its lifetime. 
Two objects with non-overlapping lifetimes may have the same id() value.
CPython implementation detail – This is the address of the object in memory
Syntax:- id(object)
Ex:- id(lst)


#                                    type ( ) Function


This function returns type of the object.
Syntax:-  type(object)
type(a)



#                             getsizeof( ) Function

This function returns the size of an object in bytes. 
The object can be any type of object. 
All built-in objects will return correct results, but this does not have to hold true for third-party extensions as it is implementation specific.
Only the memory consumption directly attributed to the object is accounted for, not the memory consumption of objects it refers to. 
This is part of sys module so you have to import sys module before using this function.
Syntax:-
from sys import *
getsizeof(object)
Ex:- from sys import *
getsizeof(a)


#                                      int ( ) Function


This function returns an integer object or return 0 if no arguments are given.
Syntax:- int(a)


#                                 float ( ) Function


This function returns an floating point number object.
Syntax:- float(a)


#                                  str ( ) Function


This function returns str version of object.
Syntax:- str(a)


#                                 list( ) Function


Rather than being a function, list is actually a mutable sequence type. This can be used in type casting to convert iterable to list.
Syntax:- list(iterable)


#                               tuple( ) Function

Rather than being a function, tuple is actually an immutable sequence type. This can be also used in type casting to convert iterable to tuple.
Syntax:- tuple(iterable)


#                               set( ) Function


This function returns a new set object, optionally with elements taken from iterable. This can be also used in type casting to convert iterable to set.
Syntax:- set(iterable)


#                              dict( ) Function

This function creates a new dictionary. This can be also used in type casting to convert iterable to dict.
Syntax:- dict(**kwarg)


#                                    len ( ) Function

This function returns the length (the number of items) of an object. 
The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
Syntax:- len(arg)
Ex:- len(lst)


#                                    min ( ) Function

This function returns the smallest item in an iterable or the smallest of two or more arguments.
If one positional argument is provided, it should be an iterable. The smallest item in the iterable is returned. If two or more positional arguments are provided, the smallest of the positional arguments is returned.
Syntax:- 
min(iterable)
min(arg1, arg2,….)
Ex:- min(lst)


#                                 max ( ) Function

This function returns the largest item in an iterable or the largest of two or more arguments.
If one positional argument is provided, it should be an iterable. The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.
Syntax:- 
max(iterable)
max(arg1, arg2,….)
Ex:- max(lst)


#                               sorted ( ) Function

This function returns a new sorted list from the items in iterable.
Syntax:- sorted(iterable)
Ex:- sorted(lst)
