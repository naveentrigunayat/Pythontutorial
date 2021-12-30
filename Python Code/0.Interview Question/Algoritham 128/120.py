'''
Python Program for factorial of a number

'''

# 1.Recursive : 

# Python 3 program to find
# factorial of given number
def factorial(n):
	
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1);

# Driver Code
num = 5;
print("Factorial of",num,"is",
factorial(num))

# This code is contributed by Smitha Dinesh Semwal


# 2.Iterative:

# Python 3 program to find
# factorial of given number
def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while(n > 1):
			fact *= n
			n -= 1
		return fact

# Driver Code
num = 5;
print("Factorial of",num,"is",
factorial(num))

# This code is contributed by Dharmik Thakkar



#  3. One line Solution (Using Ternary operator): 

# Python 3 program to find
# factorial of given number

def factorial(n):

	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1)


# Driver Code
num = 5
print ("Factorial of",num,"is",
	factorial(num))

# This code is contributed
# by Smitha Dinesh Semwal.



#  4. By using In-built function:


# Python 3 program to find
# factorial of given number
import math

def factorial(n):
	return(math.factorial(n))


# Driver Code
num = 5
print("Factorial of", num, "is",
	factorial(num))

# This code is contributed by Ashutosh Pandit



