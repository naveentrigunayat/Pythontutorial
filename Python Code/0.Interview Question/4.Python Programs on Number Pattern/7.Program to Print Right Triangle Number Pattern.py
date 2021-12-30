'''
Program to Print Right Triangle Number Pattern

'''


# Python Program to Print Right Triangle Number Pattern
 
rows = int(input("Please Enter the total Number of Rows  : "))

print("Right Triangle Pattern of Numbers") 
 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print('%d' %i, end = '  ')
    print()