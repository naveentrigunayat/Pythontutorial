'''
Program to print Palindrome numbers from 1 to 100


A palindrome number is a number that is same after reverse. For example 121, 34543, 343, 131, 48984 are the palindrome numbers.
'''

minimum = int(input(" Please Enter the Minimum Value : "))
maximum = int(input(" Please Enter the Maximum Value : "))

print("Palindrome Numbers between %d and %d are : " %(minimum, maximum))
for num in range(minimum, maximum + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10

    if(num == reverse):
        print("%d " %num, end = '  ')