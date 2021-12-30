'''

Program to find Angle of a Triangle if two angles are given

'''

'''
This python program helps the user to enter two angles of a triangle. 
Next, we subtracted those two angles from 180 because the sum of all angles in a triangle = 180.

'''


# Python Program to find Angle of a Triangle if two angles are given



a = float(input('Please Enter the First Angle of a Triangle: '))
b = float(input('Please Enter the Second Angle of a Triangle: '))

# Finding the Third Angle
c = 180 - (a + b)

print("Third Angle of a Triangle = ", c)



# Python Program to find Angle of a Triangle if two angles are given



def triangle_angle(a, b):
    return 180 - (a + b)

a = float(input('Please Enter the First Angle of a Triangle: '))
b = float(input('Please Enter the Second Angle of a Triangle: '))

# Finding the Third Angle
c = triangle_angle(a, b)
print("Third Angle of a Triangle = ", c)