'''
Generator:
Generators are functions that return a sequence of values. We use yield statement to return the value from function.


Yield Statement:
Yield statement returns the elements from a generator function into a generator object.
Ex:- yield a


next ( ) Function:
This function is used to retrieve element by element from a generator object. 
Syntax:- next(gen_obj)


'''
def show(a,b):
	while a<=b :
		yield a
		a+=1

result = show(1, 5)
print(result)
print(type(result))
	
print(next(result))
print(next(result))
print(next(result))

for i in result:
	print(i)
