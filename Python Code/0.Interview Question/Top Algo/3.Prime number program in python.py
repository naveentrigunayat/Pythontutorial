#   Prime number program in python with explanation


'''What is prime number?
In Mathematical term, A prime number is a number which can be divided by only 1 and number itself.

For example : 2, 3, 5, 7, 13,…

Here 2, 3 or any of the above number can only be divided by 1 or number itself.'''


# Program to check if a number is prime or not

#num = 407

# To take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")