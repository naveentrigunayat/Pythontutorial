#                                        Nested Tuple


A tuple within another tuple is called as nested tuple or nesting of a tuple.
Ex:- 
a = (10, 20, 30, (50, 60))

b = (50, 60)
a = (10, 20, 30, b)

a = (  (10, 20, 30), (40, 50, 60)  )
a = (  (10, 20, 30),
         (40, 50, 60)  )


#                                          Index



a = (10, 20, 30, (50, 60))

b = (50, 60)
a = (10, 20, 30, b)

a = (  (10, 20, 30), (40, 50, 60)  )
a = (  (10, 20, 30),
         (40, 50, 60)  )




#                                              Accessing Nested Tuple


a = (10, 20, 30, (50, 60))

b = (50, 60)
a = (10, 20, 30, b)
print(a[0])
print(a[1])
print(a[2])
print(a[3][0])
print(a[3][1])

print(a)		# All elements



#                                         Accessing Nested Tuple


a = (  (10, 20, 30),
         (40, 50, 60)  )
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])
print(a[1][1])
print(a[1][2])

print(a)		# All elements



#                                     Accessing Nested tuple using for loop


a = (  (10, 20, 30),
         (40, 50, 60)  )



Without index
for r in a:
       for c in r:
	print(c)
       print( )


---------------------


With index
n = len(a)
for i in range(n):
        for j in range(len(a[i])):
	print(a[i][j])
         print ( )



The outer for loop represents the rows and the inner for loop represents the columns in each row.




#                                              Accessing Nested tuple using while loop



a = (  (10, 20, 30),
         (40, 50, 60)  )
n = len(a)
i = 0
while i < n :
         j = 0
         while j < len(a[i]):
	       print(a[i][j])
	       j+=1
         i+=1
