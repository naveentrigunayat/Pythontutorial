'''
Write A Programme to find Sum from 1 to n

Solution :

'''

n = int(input("Enter Number upto Which You Want To Sum :"))

i = 1

sum = 0

while(i<=n):
    sum = sum + i
    i = i + 1

print("Sum = ", sum)