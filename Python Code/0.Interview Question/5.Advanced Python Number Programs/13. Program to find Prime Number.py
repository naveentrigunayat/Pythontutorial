'''
 Program to find Prime Number


To prove whether a number is a prime number, 
first try dividing it by 2, and see if you get a whole number. If you do, it can't be a prime number.

'''


def finding_factors(Number):
    count = 0

    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
    return count

Num = int(input(" Please Enter any Number: "))

cnt = finding_factors(Num)

if (cnt == 0 and Num != 1):
    print(" %d is a Prime Number" %Num)
else:
    print(" %d is not a Prime Number" %Num)