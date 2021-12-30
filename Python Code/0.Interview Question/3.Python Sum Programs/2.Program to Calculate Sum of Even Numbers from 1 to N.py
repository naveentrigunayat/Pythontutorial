'''
Program to Calculate Sum of Even Numbers from 1 to N

'''

minimum = int(input("Enter The Minimum Value : "))
maximum = int(input("Enter the Maximum Value : "))
total = 0

for number in range(minimum, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number

print("The Sum of Even Numbers from {0} to {1} = {2}".format(minimum,number, total))