'''

Question:

By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.

Solution:

'''

li = [12,24,35,24,88,120,155]
li.remove(24)  # this will remove only the first occurrence of 24
print(li)
