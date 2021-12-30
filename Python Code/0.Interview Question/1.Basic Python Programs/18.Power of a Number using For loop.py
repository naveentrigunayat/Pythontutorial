'''
Power of a Number using For loop

'''


import math

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))

power = math.pow(number, exponent)
    
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))