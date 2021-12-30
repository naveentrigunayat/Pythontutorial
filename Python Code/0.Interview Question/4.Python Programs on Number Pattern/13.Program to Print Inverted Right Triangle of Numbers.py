'''
Program to Print Inverted Right Triangle of Numbers

'''

# Python Program to Print Inverted Right Triangle of Numbers
 
rows = int(input("Please Enter the total Number of Rows  : "))

print("Inverted Right Triangle Pattern of Numbers") 
i = rows
while(i >= 1):
    for j in range(1, i + 1):      
        print('%d ' %i, end = '  ')
    i = i - 1
    print()