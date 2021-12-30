'''

Program to find First Digit of a Number

'''


def first_digit(number):
    while (number >= 10):
        number = number // 10
    return number

num = int(input("Please Enter any Number: "))

firstDigit = first_digit(num)

print("The First Digit from a Given Number {0} = {1}".format(num, firstDigit))