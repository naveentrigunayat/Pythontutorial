'''

Python Program to find Sum of Square of digits of a given Number


'''


# Solution


print("Enter a Number: ")
num = int(input())

sum = 0
while num!=0:
    rem = num%10
    sqr = rem*rem
    sum = sum+sqr
    num = int(num/10)

print("\nSum of squares of digits of given number is: ")
print(sum)



'''
This program is created to produce manual error message when user inputs an invalid input. The try-except block is used to do the job like shown in the program and its sample run given below:

'''

print("Enter a Number: ", end="")
try:
    num = int(input())
    temp = num
    sum = 0
    while temp!=0:
        rem = temp%10
        sqr = rem*rem
        sum = sum+sqr
        temp = int(temp/10)
    print("\nSum of squares of digits of", num, "=", sum)

except ValueError:
    print("\nInvalid Input!")


    