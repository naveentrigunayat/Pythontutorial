'''

Program to find Area of a Triangle using base and height

'''


'''
Program to find Area of a Triangle using base and height example 1
This Python program allows the user to enter the base and height of a triangle. By using the base and height values, it finds the area of a triangle. 
The mathematical formula to find Area of a triangle using base and height: Area = (base * height) / 2.


'''


# Python Program to find Area of a Triangle using base and height



base = float(input('Please Enter the Base of a Triangle: '))
height = float(input('Please Enter the Height of a Triangle: '))

# calculate the area
area = (base * height) / 2

print("The Area of a Triangle using", base, "and", height, " = ", area)



# Python Program to find Area of a Triangle using base and height




def area_of_triangle(base, height):
    return (base * height) / 2

base = float(input('Please Enter the Base of a Triangle: '))
height = float(input('Please Enter the Height of a Triangle: '))

# calculate the area
area = area_of_triangle(base, height)
print("The Area of a Triangle using", base, "and", height, " = ", area)