#  Armstrong number program in python with explanation


'''What is Armstrong Number?
It is a number which is equal to the sum of cube of its digits.
For eg: 153, 370 etc.
Lets see it practically by calculating it,

Suppose I am taking 153 for an example 

First calculate the cube of its each digits

  1^3 = (1*1*1) = 1

  5^3 = (5*5*5) = 125

  3^3= (3*3*3) = 27

Now add the cube 

  1+125+27 = 153

It means 153 is an Armstrong number.'''



# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
