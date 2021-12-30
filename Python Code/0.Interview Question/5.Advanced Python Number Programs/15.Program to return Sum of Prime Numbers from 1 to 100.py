'''
Program to return Sum of Prime Numbers from 1 to 100

'''


minimum = int(input(" Please Enter the Minimum Value: "))
maximum = int(input(" Please Enter the Maximum Value: "))
total = 0

for Number in range (minimum, maximum + 1):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
        total = total + Number

print("\n\nSum of Prime Numbers from %d to %d = %d" %(minimum, maximum, total))