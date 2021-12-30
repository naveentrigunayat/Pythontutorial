'''

Program to Swap Two Numbers


'''


def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    
    print("After Swapping two Number: num1 = {0} and num2 = {1}".format(a, b))
 
num1 = float(input(" Please Enter the First Value : "))
num2 = float(input(" Please Enter the Second Value : "))

print("Before Swapping two Number: num1 = {0} and num2 = {1}".format(num1, num2))

swap_numbers(num1, num2)