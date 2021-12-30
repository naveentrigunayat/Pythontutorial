'''
Print Star in Right Angle Triangle Shape

'''



num = int(input("Enter the Number Of Rows : "))


for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()