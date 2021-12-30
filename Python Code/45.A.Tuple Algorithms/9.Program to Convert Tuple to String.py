'''
Program to Convert Tuple to String

'''


# Tuple To String

strTuple = ('t', 'u', 't', 'o', 'r', 'i', 'a', 'l')
print("Tuple Items = ", strTuple)

strVal = ''
for t in strTuple:
    strVal = strVal + t
    
print("String from Tuple = ", strVal)

stringVal = ''
for i in range(len(strTuple)):
    stringVal = stringVal + strTuple[i]
    
print("String from Tuple = ", stringVal)



#This Python example uses the lambda function to convert the tuple items to string.

# Tuple To String

from functools import reduce

strTuple = ('t', 'u', 't', 'o', 'r', 'i', 'a', 'l', 's')
print("Tuple Items = ", strTuple)

strVal = reduce(lambda x, y: str(x) + str(y), strTuple, '')
print("String from Tuple = ", strVal)