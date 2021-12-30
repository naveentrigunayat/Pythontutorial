'''
Program to find Perimeter of a Rectangle using length and width

'''


'''
This Python program allows user to enter the length and width of a rectangle. By using the length and width, this program finds the perimeter of a rectangle. 
The math formula to calculate perimeter of a rectangle: perimeter  = 2 * (Length + Width). If we know the length & width.

'''


# Python Program to find Perimeter of a Rectangle using length and width




length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

# calculate the perimeter
perimeter = 2 * (length + width)

print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)



# Python Program to find Perimeter of a Rectangle using length and width



def perimeter_of_Rectangle(length, width):
    return 2 * (length + width)

length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

# calculate the perimeter
perimeter = perimeter_of_Rectangle(length, width)
print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)