'''
Program to find Volume and Surface Area of Cuboid

'''


'''
Python Cuboid
Cuboid is a 3D object made up of 6 Rectangles. All the opposite faces (i.e Top and Bottom) are equal.


Surface Area of a Cuboid
The Total Surface Area of a Cuboid is the sum of all the 6 rectangles areas present in the Cuboid. If we know the length, width and height of the Cuboid then we can calculate the Total Surface Area using the formula:

Area of Top & Bottom Surfaces = lw + lw = 2lw

Area of Front & Back Surfaces = lh + lh = 2lh


Area of both sides = wh + wh = 2wh

The Total Surface Area of a Cuboid is the sum of all the 6 faces. So, we have to add all these area to calculate the final Surface Area

Total Surface Area of a Cuboid = 2lw + 2lh + 2wh


It is equal: Total Surface Area = 2 (lw + lh +wh)

Volume of a Cuboid
The amount of space inside the Cuboid is called as Volume. If we know the length, width and height of the Cuboid then we can calculate the Volume using the formula:

Volume of a Cuboid = Length * Breadth * Height

Volume of a Cuboid = lbh

The Lateral Surface Area of a Cuboid = 2h (l + w)

'''



# Python Program to find Volume and Surface Area of Cuboid

length = float(input('Please Enter the Length of a Cuboid: '))
width = float(input('Please Enter the Width of a Cuboid: '))
height = float(input('Please Enter the Height of a Cuboid: '))

# Calculate the Surface Area
SA = 2 * (length * width + length * height + width * height)

# Calculate the Volume
Volume = length * width * height

# Calculate the Lateral Surface Area
LSA = 2 * height * (length + width)

print("\n The Surface Area of a Cuboid = %.2f " %SA)
print(" The Volume of a Cuboid = %.2f" %Volume);
print(" The Lateral Surface Area of a Cuboid = %.2f " %LSA)



# Python Program to find Volume and Surface Area of a Cuboid using Functions

def Vo_Sa_Cuboid(length, width, height):
    # Calculate the Surface Area
    SA = 2 * (length * width + length * height + width * height)

    # Calculate the Volume
    Volume = length * width * height

    # Calculate the Lateral Surface Area
    LSA = 2 * height * (length + width)

    print("\n The Surface Area of a Cuboid = %.2f " %SA)
    print(" The Volume of a Cuboid = %.2f" %Volume)
    print(" The Lateral Surface Area of a Cuboid = %.2f " %LSA)

Vo_Sa_Cuboid(9, 4, 6)