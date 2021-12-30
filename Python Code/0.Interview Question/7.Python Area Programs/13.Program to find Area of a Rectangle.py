'''
Program to find Area of a Rectangle

'''

'''
If we know the width and height then, we can calculate the area of a rectangle using below formula.


Area = Width * Height

Perimeter is the distance around the edges. We can calculate perimeter of a rectangle using below formula

Perimeter = 2 * (Width + Height)


'''


# Python Program to find Area of a Rectangle




width = float(input('Please Enter the Width of a Rectangle: '))
height = float(input('Please Enter the Height of a Rectangle: '))

# calculate the area
Area = width * height

# calculate the Perimeter
Perimeter = 2 * (width + height)

print("\n Area of a Rectangle is: %.2f" %Area)
print(" Perimeter of Rectangle is: %.2f" %Perimeter)



# Python Program to find Area of a Rectangle using Functions




def Area_of_a_Rectangle(width, height):

    # calculate the area
    Area = width * height

    # calculate the Perimeter
    Perimeter = 2 * (width + height)

    print("\n Area of a Rectangle is: %.2f" %Area)
    print(" Perimeter of Rectangle is: %.2f" %Perimeter)

Area_of_a_Rectangle(6, 4)