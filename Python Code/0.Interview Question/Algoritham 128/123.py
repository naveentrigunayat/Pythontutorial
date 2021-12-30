'''
Python Program to Reverse a String Using For Loop

'''

#                                             Using loop

# Python code to reverse a string
# using loop

def reverse(s):
str = ""
for i in s:
	str = i + str
return str

s = "Geeksforgeeks"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (reverse(s))



#                                 using Recursion


# Python code to reverse a string
# using recursion

def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]

s = "Geeksforgeeks"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))



#                                           Using extended slice syntax



# Python code to reverse a string
# using extended slice syntax

# Function to reverse a string
def reverse(string):
	string = string[::-1]
	return string

s = "Geeksforgeeks"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using extended slice syntax) is : ",end="")
print (reverse(s))





#                                     Using reversed


# Python code to reverse a string
# using reversed()

# Function to reverse a string
def reverse(string):
	string = "".join(reversed(string))
	return string

s = "Geeksforgeeks"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using reversed) is : ",end="")
print (reverse(s))
