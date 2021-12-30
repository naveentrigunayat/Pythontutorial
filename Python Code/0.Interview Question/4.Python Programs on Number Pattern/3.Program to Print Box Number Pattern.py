'''
Program to Print Box Number Pattern

'''

# Python Program to Print Box Number Pattern of 1 and 0
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Box Number Pattern of 1 and 0") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i == 1 or i == rows or j == 1 or j == columns):          
            print('1', end = '  ')
        else:
            print('0', end = '  ')
    print()



# Program for Box Number Pattern of 0 and 1

rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Box Number Pattern of 1 and 0") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i == 1 or i == rows or j == 1 or j == columns):          
            print('0', end = '  ')
        else:
            print('1', end = '  ')
    print()



