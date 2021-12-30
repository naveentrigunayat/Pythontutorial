'''
Python Program to Print Fibonacci Series

'''

#   Method 1 ( Use recursion ) :  

# Function for nth Fibonacci number
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

# Driver Program
print(Fibonacci(9))

# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya



#      Method 2 ( Use Dynamic Programming ) :  


# Function for nth fibonacci
# number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1
FibArray = [0, 1]

def fibonacci(n):

	# Check is n is less
	# than 0
	if n <= 0:
		print("Incorrect input")
		
	# Check is n is less
	# than len(FibArray)
	elif n <= len(FibArray):
		return FibArray[n - 1]
	else:
		temp_fib = fibonacci(n - 1) +
					fibonacci(n - 2)
		FibArray.append(temp_fib)
		return temp_fib

# Driver Program
print(fibonacci(9))

# This code is contributed by Saket Modi



#    Method 3 ( Space Optimized):  


# Function for nth fibonacci
# number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
	a = 0
	b = 1
	
	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")
		
	# Check is n is equal
	# to 0
	elif n == 0:
		return 0
	
	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program
print(fibonacci(9))

# This code is contributed by Saket Modi
# Then corrected and improved by Himanshu Kanojiya



