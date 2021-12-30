'''
Write a programme to find Sum of Even Numbers


Solution :

'''

n = int(input("Enter A Number Upto Which You want To add Even numbers : "))

i = 1
sum = 0
while (i<=n):
    if (i%2==0):
        sum = sum + i

    i = i + 1

print("Sum of Even Numbers :" , sum)