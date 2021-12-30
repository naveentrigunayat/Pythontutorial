'''
Accessing using for loop:

a = (10, 20, -50, 21.3, ‘Geekyshows’)

Without index
for element in a:
	print(element)

With index
n = len(a)
for i in range(n):
	print(a[i])

'''

# Access Tuple using for Loop
a = (10, 21.3, 'Geekyshows')		

# Without Index
print("Access Without Index")
for element in a:
	print(element)

print()
	
# With Index
print("Access With Index")
n = len(a)
for i in range(n):
	print(i,a[i])
