'''

Program to find Last Digit in a Number

'''


def lastDigit(num):
    return num % 10

number = int(input("Please Enter any Number: "))

last_digit = lastDigit(number)

print("The Last Digit in a Given Number %d = %d" %(number, last_digit))