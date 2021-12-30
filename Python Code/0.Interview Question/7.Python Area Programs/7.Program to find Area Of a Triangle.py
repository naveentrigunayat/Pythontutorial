'''

Program to find Area Of a Triangle

'''


'''

Area Of a Triangle
If we know the length of three sides of a triangle then we can calculate the area of a triangle using Heron’s Formula


Area of a Triangle = √(s*(s-a)*(s-b)*(s-c))

Where s = (a + b + c )/ 2 (Here s = semi perimeter and a, b, c are the three sides of a triangle)

Perimeter of a Triangle = a + b + c


'''

'''

This Python program allows the user to enter three sides of the triangle
Using those values we will calculate the Perimeter of a triangle, Semi Perimeter of a triangle and then Area of a Triangle.

# Program to find Area of a Triangle & Perimeter of a Triangle

'''



a = float(input('Please Enter the First side of a Triangle: '))
b = float(input('Please Enter the Second side of a Triangle: '))
c = float(input('Please Enter the Third side of a Triangle: '))

# calculate the Perimeter
Perimeter = a + b + c

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("\n The Perimeter of Traiangle = %.2f" %Perimeter);
print(" The Semi Perimeter of Traiangle = %.2f" %s);
print(" The Area of a Triangle is %0.2f" %Area)





# Python Program to find Area of a Triangle using Functions



import math

def Area_of_Triangle(a, b, c):
    
    # calculate the Perimeter
    Perimeter = a + b + c
    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))

    print("\n The Perimeter of Traiangle = %.2f" %Perimeter);
    print(" The Semi Perimeter of Traiangle = %.2f" %s);
    print(" The Area of a Triangle is %0.2f" %Area)

Area_of_Triangle(6, 7, 8)