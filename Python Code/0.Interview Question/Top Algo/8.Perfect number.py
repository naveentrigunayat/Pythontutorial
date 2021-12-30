#                           Perfect number 


'''What is Perfect Number?
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.

 

Lets understand it with example

6 is a positive number and its divisor is 1,2,3 and 6 itself.

But we should not include 6 as by the definition of perfect number.

Lets add its divisor excluding itself

1+2+3 = 6 which is equal to number itself.

It means 6 is a Perfect Number.'''


num = int(input("please give first number a: "))
sum=0
for i in range(1,(num//2)+1):
    remainder = num % i
    if remainder == 0:
        sum = sum + i
if sum == num:
    print("given no. is perfect number")
else:
    print("given no. is not a perfect number") 