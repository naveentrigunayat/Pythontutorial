'''
Program To find Area Of Circle

'''


# Python Program to find Area Of Circle using Radius




PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
area = PI * radius * radius
circumference = 2 * PI * radius

print(" Area Of a Circle = %.2f" %area)
print(" Circumference Of a Circle = %.2f" %circumference)



# Python Program to find Area Of Circle using Circumference



import math

circumference = float(input(' Please Enter the Circumference of a circle: '))
area = (circumference * circumference)/(4 * math.pi)

print(" Area Of a Circle = %.2f" %area)



# Python Program to find Area Of Circle using Diameter



import math

diameter = float(input(' Please Enter the Diameter of a circle: '))
area1 = (math.pi/4) * (diameter * diameter)
# diameter = 2 * radius
# radius = diameter/2
radius = diameter / 2
area2 = math.pi * radius * radius

print(" Area of Circle using direct formula = %.2f" %area1);
print(" Area of Circle Using Method 2 = %.2f" %area2)