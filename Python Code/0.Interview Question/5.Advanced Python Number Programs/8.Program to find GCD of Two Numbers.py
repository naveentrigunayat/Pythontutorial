'''
Program to find GCD or HCF of Two Numbers

The GCD is a mathematical term for the Greatest Common Divisor of two or more numbers. 
It is the Greatest common divisor that completely divides two or more numbers without leaving any remainder. 
Therefore, it is also known as the Highest Common Factor (HCF) of two numbers. 
For example, the GCD of two numbers, 20 and 28, is 4 because both 20 and 28 are completely divisible by 1, 2, 4 (the remainder is 0), 
and the largest positive number among the factors 1, 2, and 4 is 4. Similarly, the GCD of two numbers, 24 and 60, is 12.

'''


def findgcd(num1, num2):
    if(num1 == 0):
        print("\n HCF of {0} and {1} = {2}".format(a, b, b))

    while(num2 != 0):
        if(num1 > num2):
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

gcd = findgcd(a, b)  
print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))