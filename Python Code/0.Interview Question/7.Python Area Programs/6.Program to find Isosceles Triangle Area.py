'''
Program to find Isosceles Triangle Area

'''


# Python Program to find Isosceles Triangle Area



import math

a = float(input("Enter Isosceles Triangle SideLength  : "))

b = float(input("Enter the Other Side of Isosceles Triangle : "))

isosceleArea = (b * math.sqrt((4 * a * a) - (b * b)))/4;

print("The Area of the Isosceles Triangle = %.3f" %isosceleArea) 



# Python Program to find Isosceles Triangle Area



import math

def IsoscelesTriangleArea(a, b):
    return (b * math.sqrt((4 * a * a) - (b * b)))/4

a = float(input("Enter Isosceles Triangle Side Length  : "))

b = float(input("Enter the Other Side of Isosceles Triangle : "))

isosceleArea = IsoscelesTriangleArea(a, b)

print("The Area of the Isosceles Triangle = %.3f" %isosceleArea) 