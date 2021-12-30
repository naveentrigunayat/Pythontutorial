'''
Program to calculate Sum of Series 1³+2³+3³+….+n³

'''


'''

Write a Python Program to calculate Sum of Series 1³+2³+3³+….+n³ using For Loop and Functions with an example.

The Mathematical formula for Python Sum of series 1³+2³+3³+….+n³ = ( n (n+1) / 6)²

'''


# Python Program to calculate Sum of Series 1³+2³+3³+….+n³
import math 

number = int(input("Please Enter any Positive Number  : "))
total = 0

total = math.pow((number * (number + 1)) /2, 2)

print("The Sum of Series upto {0}  = {1}".format(number, total))


# Python Program to calculate Sum of Series 1³+2³+3³+….+n³
import math 

number = int(input("Please Enter any Positive Number  : "))
total = 0

total = math.pow((number * (number + 1)) /2, 2)

for i in range(1, number + 1):
    if(i != number):
        print("%d^3 + " %i, end = ' ')
    else:
        print("{0}^3 = {1}".format(i, total))




# Python Program to calculate Sum of Series 1³+2³+3³+….+n³
import math 

def sum_of_cubes_series(number):
    total = 0

    total = math.pow((number * (number + 1)) /2, 2)

    for i in range(1, number + 1):
        if(i != number):
            print("%d^3 + " %i, end = ' ')
        else:
            print("{0}^3 = {1}".format(i, total))

num = int(input("Please Enter any Positive Number  : "))
sum_of_cubes_series(num)



# Python Program to calculate Sum of Series 1³+2³+3³+….+n³

def sum_of_cubes_series(number):
    if(number == 0):
        return 0
    else:
        return (number * number * number) + sum_of_cubes_series(number - 1)

num = int(input("Please Enter any Positive Number  : "))
total = sum_of_cubes_series(num)

print("The Sum of Series upto {0}  = {1}".format(num, total))