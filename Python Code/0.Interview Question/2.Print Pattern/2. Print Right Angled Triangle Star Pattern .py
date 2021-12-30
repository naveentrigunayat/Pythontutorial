'''

 Printing Stars '*' in Right Angle Triangle Shape

'''


num = int(input("Enter number of Rows : "))

k = 1

for i in range(1,num+1):
    for j in range(1,k+1):
        print("1",end=" ")
    k = k + 2
    print()