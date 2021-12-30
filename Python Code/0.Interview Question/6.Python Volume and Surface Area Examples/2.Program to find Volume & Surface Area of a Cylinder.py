'''
Program to find Volume & Surface Area of a Cylinder


'''





'''
Surface Area of a Cylinder
If we know the radius and height of the cylinder then we can calculate the surface area of a cylinder using the formula:


Surface Area of a Cylinder = 2πr² + 2πrh (Where r is radius and h is the height of the cylinder).

Volume of a Cylinder
The amount of space inside the Cylinder is called as Volume. If we know the height of a cylinder then we can calculate the Volume of a cylinder using formula:

Volume of a Cylinder = πr²h


The Lateral Surface Area of a Cylinder = 2πrh

We can calculate the Top Or Bottom Surface Area of a Cylinder = πr²

'''



# Python Program to find Volume & Surface Area of a Cylinder

PI = 3.14
radius = float(input('Please Enter the Radius of a Cylinder: '))
height = float(input('Please Enter the Height of a Cylinder: '))

sa = 2 * PI * radius * (radius + height)
Volume = PI * radius * radius * height
L = 2 * PI * radius * height
T = PI * radius * radius

print("\n The Surface area of a Cylinder = %.2f" %sa)
print(" The Volume of a Cylinder = %.2f" %Volume)
print(" Lateral Surface Area of a Cylinder = %.2f" %L);
print(" Top OR Bottom Surface Area of a Cylinder = %.2f" %T)




# Python Program to find Volume & Surface Area of a Cylinder using Functions

import math

def Vol_Sa_Cylinder(radius, height):
    sa = 2 * math.pi * radius * (radius + height)
    Volume = math.pi * radius * radius * height
    L = 2 * math.pi * radius * height
    T = math.pi * radius * radius

    print("\n The Surface area of a Cylinder = %.2f" %sa)
    print(" The Volume of a Cylinder = %.2f" %Volume)
    print(" Lateral Surface Area of a Cylinder = %.2f" %L)
    print(" Top OR Bottom Surface Area of a Cylinder = %.2f" %T)

Vol_Sa_Cylinder(6, 4)