'''
 Palindrome Program using Functions

A palindrome number is a number that is same after reverse. For example 121, 34543, 343, 131, 48984 are the palindrome numbers.
'''


def integer_reverse(number):
    reverse = 0
    
    while(number > 0):
        Reminder = number % 10
        reverse = (reverse * 10) + Reminder
        number = number // 10
    return reverse

number = int(input("Please Enter any Number: "))

rev = integer_reverse(number)
print("Reverse of a Given number is = %d" %rev)

if(number == rev):
    print("%d is a Palindrome Number" %number)
else:
    print("%d is not a Palindrome Number" %number)