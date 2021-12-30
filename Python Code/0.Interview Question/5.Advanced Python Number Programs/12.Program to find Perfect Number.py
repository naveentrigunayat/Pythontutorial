'''
Program to find Perfect Number


Perfect number, a positive integer that is equal to the sum of its proper divisors. 
The smallest perfect number is 6, which is the sum of 1, 2, and 3

'''


def Perfect_Number(Number):
    Sum = 0
    for i in range(1, Number):
        if(Number % i == 0):
            Sum = Sum + i
    return Sum        

# Taking input from the user
Number = int(input("Please Enter any number: "))
if (Number == Perfect_Number(Number)):
    print("\n %d is a Perfect Number" %Number)
else:
    print("\n %d is not a Perfect Number" %Number)