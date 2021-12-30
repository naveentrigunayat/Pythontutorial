'''
Program to find Volume and Surface Area of a Cone

'''

'''

Python Surface Area of a Cone
If we know the radius and Slant of a Cone then we calculate the Surface Area of Cone using the below formula:
Surface Area = Area of the Cone + Area of Circle
Surface Area = πrl + πr²
Where r = radius and
l = Slant (Length of an edge from top of the cone to edge of a cone)


If we know the radius and height of a Cone then we calculate the Surface Area of Cone using the below formula:
Surface Area = πr² +πr √h² + r²
We can also write it as:
Surface Area = πr (r+√h² + r²)

Because radius, height and Slant make the shape as right-angled Triangle. So, Using the Pythagoras theorem:
l² = h² + r²
l = √h² + r²

Python Volume of a Cone
The amount of space inside the Cone is called as Volume. If we know the radius and height of the Cone then we can calculate the Volume using the formula:
Volume = 1/3 πr²h (where h= height of a Cone)


The Lateral Surface Area of a Cone = πrl


'''


# Python Program to find Volume and Surface Area of a Cone

import math

radius = float(input('Please Enter the Radius of a Cone: '))
height = float(input('Please Enter the Height of a Cone: '))

# Calculate Length of a Slide (Slant)
l = math.sqrt(radius * radius + height * height)

# Calculate the Surface Area
SA = math.pi * radius * (radius + l)

# Calculate the Volume
Volume = (1.0/3) * math.pi * radius * radius * height

# Calculate the Lateral Surface Area
LSA = math.pi * radius  * l

print("\n Length of a Side (Slant)of a Cone = %.2f" %l)
print(" The Surface Area of a Cone = %.2f " %SA)
print(" The Volume of a Cone = %.2f" %Volume);
print(" The Lateral Surface Area of a Cone = %.2f " %LSA)



# Python Program to find Volume and Surface Area of a Cone using functions

import math

def Vo_Sa_Cone(radius, height):
    # Calculate Length of a Slide (Slant)
    l = math.sqrt(radius * radius + height * height)

    # Calculate the Surface Area
    SA = math.pi * radius * (radius + l)

    # Calculate the Volume
    Volume = (1.0/3) * math.pi * radius * radius * height

    # Calculate the Lateral Surface Area
    LSA = math.pi * radius  * l

    print("\n Length of a Side (Slant)of a Cone = %.2f" %l)
    print(" The Surface Area of a Cone = %.2f " %SA)
    print(" The Volume of a Cone = %.2f" %Volume)
    print(" The Lateral Surface Area of a Cone = %.2f " %LSA)

Vo_Sa_Cone(6,10)