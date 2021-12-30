'''
Tuple:

Tuple – A tuple contains a group of elements which can be same or different types. 
Tuples are immutable. 
It is similar to List but Tuples are read-only which means we can not modify it’s element. 
Tuples are used to store data which should not be modified. 
It occupies less memory compare to list.
Tuples are represented using parentheses ( ).
Ex:- a = (10, 20, -50, 21.3, ‘Geekyshows’)


Creating Empty Tuple:

Syntax:- tuple_name = ( )
Ex:- a = ( )



Creating Tuple:

We can create tuple by writing elements separated by commas inside parentheses.

With one Element
b = (10)               <------ It will become integer
c  = (10, )

With Multiple Elements
d = (10, 20, 30, 40)
e = (10, 20, -50, 21.3, ‘GeekyShows’)
f = 10, 20, -50, 21.3, ‘GeekyShows’        <----  It will become a tuple 



Index:

An index represents the position number of an tuple’s element. The index start from 0 on wards and written inside square braces.
Ex:- a = (10, 20, -50, 21.3, ‘Geekyshows’)



Accessing Tuple’s Element:

a = (10, 20, -50, 21.3, ‘Geekyshows’)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

'''

# Tuple
# Creating Empty Tuple
a = ()

# Creating Tuple with one element
b = (10)			# It will become an integer
c = (10,)			# for creating single element tuple write comma

# Creating Tuple with Multiple element
d = (10, 20, 30, 40)
e = (10, 20, -50, 21.3, 'GeekyShows')		
f = 10, 20, -50, 21.3, 'GeekyShows'			# tuple e and f are same

print()
# Access using index
print("Accessing Tuple d:")
print("d[0] =", d[0])
print("d[1] =", d[1])
print("d[2] =", d[2])
print("d[3] =", d[3])
print()

print("Accessing Tuple e:")
print("e[0] =", e[0])
print("e[1] =", e[1])
print("e[2] =", e[2])
print("e[3] =", e[3])
print("e[4] =", e[4])
print()

print("Accessing Tuple f:")
print("f[0] =", f[0])
print("f[1] =", f[1])
print("f[2] =", f[2])
print("f[3] =", f[3])
print("f[4] =", f[4])

