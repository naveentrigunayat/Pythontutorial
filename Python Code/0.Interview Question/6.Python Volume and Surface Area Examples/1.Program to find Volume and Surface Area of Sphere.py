'''
Program to find Volume and Surface Area of Sphere

'''


'''
Python Surface Area of Sphere
A Sphere looks like a basketball or we can say the three-dimensional view of a circle. If we know the radius of the Sphere then we can calculate the Surface Area of Sphere using formula:


Surface Area of a Sphere = 4πr² (Where r is radius of the sphere).

From the above formula, If we know the Surface Area of a sphere then we can calculate the radius of a Sphere using the formula:

Radius of a Sphere = √sa / 4π (Where sa is the Surface Area of a sphere).


Python Volume of Sphere
Amount of space inside the sphere is called as Volume. If we know the radius of the Sphere then we can calculate the Volume of Sphere using formula:

Volume of a Sphere = 4πr³

'''


# Python Program to find Volume and Surface Area of Sphere

PI = 3.14
radius = float(input('Please Enter the Radius of a Sphere: '))
sa =  4 * PI * radius * radius
Volume = (4 / 3) * PI * radius * radius * radius

print("\n The Surface area of a Sphere = %.2f" %sa)
print("\n The Volume of a Sphere = %.2f" %Volume)



# Python Program to find Volume and Surface Area of Sphere using Functions

import math

def Area_of_Triangle(radius):
    sa =  4 * math.pi * radius * radius
    Volume = (4 / 3) * math.pi * radius * radius * radius
    print("\n The Surface area of a Sphere = %.2f" %sa)
    print("\n The Volume of a Sphere = %.2f" %Volume)

Area_of_Triangle(6)