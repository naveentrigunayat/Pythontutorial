'''

Program to find Factorial of a Number

'''


def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


number = int(input(" Please enter any Number to find factorial : "))

facto = factorial(number)
print("The factorial of %d  = %d" %(number, facto))