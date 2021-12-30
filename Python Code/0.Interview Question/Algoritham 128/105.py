'''

Write A prgramme to find Sum of square from 1 to n 

solution :

'''

n = int(input("Enter Number upto which you want to sum :"))

i = 1
sum = 0

while(i<=n):
    sum = sum + (i*i)
    i = i + 1

print("Sum =",sum)