'''
Program to Print 1 and 0 in alternative Columns 

'''


# Python Program to Print 1 and 0 in alternative Columns
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative Columns") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(j % 2 == 0):          
            print('0', end = '  ')
        else:
            print('1', end = '  ')
    print()



# Python Program to Print 1 and 0 in alternative Columns without IF
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative Columns") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print('%d' %(j % 2), end = '  ')
    print()



# Python Program to Print 1 and 0 in alternative Columns
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative Columns") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(j % 2 != 0):          
            print('0', end = '  ')
        else:
            print('1', end = '  ')
    print()