'''

Program to find Diameter Circumference and Area Of a Circle

'''


'''

Write Python Program to find Diameter Circumference and Area Of a Circle with a practical example. The mathematical formulas are:

Diameter of a Circle = 2r = 2 * radius
Area of a circle is: A = πr² =  π * radius * radius
Circumference of a Circle = 2πr = 2 * π * radius

'''


# Python Program to find Diameter, Circumference, and Area Of a Circle

PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))

diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

print(" \nDiameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)



# Python Program to find Diameter, Circumference, and Area Of a Circle



import math

def find_Diameter(radius):
    return 2 * radius

def find_Circumference(radius):
    return 2 * math.pi * radius

def find_Area(radius):
    return math.pi * radius * radius

r = float(input(' Please Enter the radius of a circle: '))

diameter = find_Diameter(r)
circumference = find_Circumference(r)
area = find_Area(r)

print("\n Diameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)