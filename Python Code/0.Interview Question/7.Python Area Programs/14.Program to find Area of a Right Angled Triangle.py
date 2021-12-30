'''

Python Area of a Right Angled Triangle
If we know the width and height then, we can calculate the area of a right angled triangle using below formula.


Area = (1/2) * width * height

Using Pythagoras formula we can easily find the unknown sides in the right angled triangle.

c² = a² + b²


Perimeter is the distance around the edges. We can calculate perimeter using below formula

Perimeter = a + b+ c


'''



# Python Program to find Area of a Right Angled Triangle



import math

width = float(input('Please Enter the Width of a Right Angled Triangle: '))
height = float(input('Please Enter the Height of a Right Angled Triangle: '))

# calculate the area
Area = 0.5 * width * height

# calculate the Third Side
c = math.sqrt((width*width) + (height*height))

# calculate the Perimeter
Perimeter = width + height + c

print("\n Area of a right angled triangle is: %.2f" %Area)
print(" Other side of right angled triangle is: %.2f" %c)
print(" Perimeter of right angled triangle is: %.2f" %Perimeter)



# Python Program to find Area of a Right Angled Triangle using Functions




import math

def Area_of_a_Right_Angled_Triangle(width, height):
    # calculate the area
    Area = 0.5 * width * height

    # calculate the Third Side
    c = math.sqrt((width * width) + (height * height))
    # calculate the Perimeter
    Perimeter = width + height + c

    print("\n Area of a right angled triangle is: %.2f" %Area)
    print(" Other side of right angled triangle is: %.2f" %c)
    print(" Perimeter of right angled triangle is: %.2f" %Perimeter)

Area_of_a_Right_Angled_Triangle(9, 10)