'''
Program to Print 1 and 0 in alternative rows

'''


# Python Program to Print 1 and 0 in alternative rows
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative rows") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i % 2 != 0):          
            print('1', end = '  ')
        else:
            print('0', end = '  ')
    print()


# Program to Display 1 and 0 in alternative rows without If

rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 1 and 0 in alternative rows") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print('%d' %(i % 2), end = '  ')
    print()


# Python Program to Print 1 and 0 in alternative rows
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Print Number Pattern - 0 and 1 in alternative rows") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i % 2 != 0):          
            print('0', end = '  ')
        else:
            print('1', end = '  ')
    print()