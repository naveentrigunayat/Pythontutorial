'''
map ( ) Function – This function executes a specified function on each element of the iterable (sequence) and perhaps changes the elements.
Syntax:-
map(function_name, iterable )
Function_name - It’s name of a function which perform an operation on all the elements of the sequence and modified elements are returned
 which can be stored in another sequence.
iterable – Iterable may be either a sequence, list, string, tuple, a container which supports iteration, or an iterator.

'''

a = [10, 20, 30, 40, 50]

# Without Lambda
def inc(n):
	return n+2
	
result = list(map(inc, a))
print(result)
print(type(result))

# With Lambda
result = list(map(lambda n: n+2, a))
print(result)
print(type(result))

