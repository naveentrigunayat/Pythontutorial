'''
Program to find Volume and Surface Area of a Cube

'''


'''
Python Cube
All the edges in the Cube has same length. OR We can say, Cube is nothing but 6 equal squares.


Surface Area of a Cube
If we know the length of any edge in Cube then we can calculate the surface area of a Cube using the formula:

Surface Area of a Cube = 6l² (Where l is the Length of any side of a Cube).

Area of a square = l² Since the Cube is made of 6 equal squares, Surface Area of a Cube = 6l²


If we already know the Surface Area of Cube. And then, we can calculate the length of any side by altering the above Python formula as:

l = √sa / 6 (sa = Surface Area of a Cube)

Volume of a Cube
The amount of space inside the Cube is called as Volume. If we know the length of any edge of a Cube then we can calculate the Volume of Cube using formula:



Volume = l * l * l

The Lateral Surface Area of a Cube = 4 * (l * l)

'''


# Python Program to find Volume and Surface Area of a Cube

l = float(input('Please Enter the Length of any Side of a Cube: '))

sa = 6 * (l * l)
Volume = l * l * l
LSA = 4 * (l * l)

print("\n Surface Area of Cube = %.2f" %sa)
print(" Volume of cube = %.2f" %Volume)
print(" Lateral Surface Area of Cube = %.2f" %LSA)



# Python Program to find Volume and Surface Area of a Cube Using Functions

def Vo_Sa_Cone(l):
    sa = 6 * (l * l)
    Volume = l * l * l
    LSA = 4 * (l * l)

    print("\n Surface Area of Cube = %.2f" %sa)
    print(" Volume of cube = %.2f" %Volume)
    print(" Lateral Surface Area of Cube = %.2f" %LSA)

Vo_Sa_Cone(6)