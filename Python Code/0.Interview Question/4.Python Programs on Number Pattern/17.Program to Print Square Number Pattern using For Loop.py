'''
Program to Print Square Number Pattern using For Loop

'''


# Python Program to Print Square Number Pattern
 
side = int(input("Please Enter any Side of a Square  : "))

print("Square Number Pattern") 

for i in range(side):
    for i in range(side):
        print('1', end = '  ')
    print()



## Python Program to Print Square Number Pattern
 
side = int(input("Please Enter any Side of a Square  : "))
number = int(input("Please Enter any Number  : "))

print("Square Number Pattern") 

for i in range(side):
    for i in range(side):
        print(number, end = '  ')
    print()