
'''

filter ( ) Function – The filter function is used to filter out the elements of an iterable (sequence)
 depending on a function that tests each element in the sequence to be true or not. 
It returns those elements of sequence, for which function is true. 
Syntax:- 
filter(function_name, iterable)
Function_name – It’s name of a function which tests each element in the sequence return True or False.
 If function is None, returns the elements that are true.
iterable – Iterable may be either a sequence, list, string, tuple, a container which supports iteration, or an iterator.


'''
a = [10, 50, 60, 80, 90, 5, 45, 65]

# Without Lambda
def high_marks(n):
	if n >= 60:
		return True

result = list(filter(high_marks,a))
print(result)
print(type(result))

print()

# With Lambda
result = list(filter(lambda n : (n>=60),a))
print(result)
print(type(result))




