'''
Program to find Area of a Rectangle using length and width

'''


'''

This Python program allows user to enter the length and width of a rectangle. Using those two values, it finds the area of a rectangle. 
If we know the length & width of a rectangle. The mathematical formula to calculate the area of a rectangle is: Area = Length * Width.

'''


# Python Program to find Area of a Rectangle using length and width



length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

# calculate the area
area = length * width

print("The Area of a Rectangle using", length, "and", width, " = ", area)



# Python Program to find Area of a Rectangle using length and width




def area_of_Rectangle(length, width):
    return length * width
length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

# calculate the area of a Rectangle
area = area_of_Rectangle(length, width)

print("The Area of a Rectangle using", length, "and", width, " = ", area)