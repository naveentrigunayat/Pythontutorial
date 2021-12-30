#                                   Nested List


A list within another list is called as nested list or nesting of a list.
Ex:- 
a = [10, 20, 30, [50, 60]]

b = [50, 60]
a = [10, 20, 30, b]

a = [  [10, 20, 30], [40, 50, 60]  ]
a = [  [10, 20, 30],
         [40, 50, 60]  ]



#                                       Index


a = [10, 20, 30, [50, 60]]

b = [50, 60]
a = [10, 20, 30, b]

a = [  [10, 20, 30], [40, 50, 60]  ]
a = [  [10, 20, 30],
         [40, 50, 60]  ]




#                                            Accessing Nested List



a = [10, 20, 30, [50, 60]]

b = [50, 60]
a = [10, 20, 30, b]
print(a[0])
print(a[1])
print(a[2])
print(a[3][0])
print(a[3][1])

print(a)		# All elements


-----------------------------------------


a = [  [10, 20, 30],
         [40, 50, 60]  ]
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])
print(a[1][1])
print(a[1][2])

print(a)		# All elements



#                                                Modifying Nested List


a = [10, 20, 30, [50, 60]]

b = [50, 60]
a = [10, 20, 30, b]

a[1] = 100
a[3][0] = 5



-----------------------


a = [  [10, 20, 30],
         [40, 50, 60]  ]

a[0][1] = 2
a[1][2] = 6




#                                                   Accessing Nested list using for loop


a = [  [10, 20, 30],
         [40, 50, 60]  ]




Without index
for r in a:
       for c in r:
	print(c)
       print( )




-------------------------




With index
n = len(a)
for i in range(n):
        for j in range(len(a[i])):
	print(a[i][j])
         print ( )




The outer for loop represents the rows and the inner for loop represents the columns in each row.




#                                              Accessing Nested list using while loop


a = [  [10, 20, 30],
         [40, 50, 60]  ]
n = len(a)
i = 0
while i < n :
         j = 0
         while j < len(a[i]):
	       print(a[i][j])
	       j+=1
         i+=1




#                                                 List ( ) Function


This is used to create a list. It returns a mutable list of elements.
Syntax:-
list()        <----  Creates Empty List

list(iterable_object)     <------  Creates a list of elements 

Ex:- 
list()
list(“GeekyShows”)


#                                      List ( ) Function

We can use list and range function to create a list.
Syntax:-
list(range(start,stop,stepsize))
Ex:- 
list(range(0, 5))
