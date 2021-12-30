'''
#                                       Copying Tuple


We can copy elements of tuple into another tuple using slice.
a = (10, 20, 30, 40, 50)
b = a
b = a[0:5]
b = a[1:4]


'''


# Copying Tuple
a = (10, 20, 30, 40, 50)
b = a
print("A:", a)
print("B:", b)
print("Id of A:", id(a))
print("Id of B:", id(b))

# if Same data then same object same id
# if data modified it creates new object new id

print()
b = a[0:5]
print("A:", a)
print("B:", b)
print("Id of A:", id(a))
print("Id of B:", id(b))