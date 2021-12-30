'''

write a programme to find sum of cubes from 1 to n

Solution :

'''


n = int(input("Enter number upto which you want to sum :"))
i = 1
sum = 0

while(i<=n):
    cube = (i*i*i)
    print(cube)
    sum = sum + cube
    i = i + 1

print("Sum =",sum)