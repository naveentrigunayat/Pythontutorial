'''

Program to find Area of an Equilateral Triangle

'''


'''

Area of an Equilateral Triangle Formula
The Equilateral Triangle is a triangle with all sides are equal and all of the angles are equal to 60 degrees. If we know the side of an Equilateral Triangle then, we can calculate the area of an Equilateral Triangle using below formula.


Area = (√3)/4 * s² (S = Any side of the Equilateral Triangle)

Perimeter is the distance around the edges. We can calculate perimeter using below formula:

Perimeter = 3s


We can calculate Semi Perimeter of an Equilateral Triangle using the formula: 3s/2 or we can simply say Perimeter/2.

We can calculate Altitude of an Equilateral Triangle using the formula: (√3)/2 * s


'''


# Python Program to find Area of an Equilateral Triangle



import math

side = float(input('Please Enter Length of any side of an Equilateral Triangle: '))

# calculate the area
Area = (math.sqrt(3)/ 4)*(side * side)

# calculate the Perimeter
Perimeter = 3 * side

# calculate the semi-perimeter
Semi = Perimeter / 2

# calculate the Altitude
Altitude = (math.sqrt(3)/2)* side

print("\n Area of Equilateral Triangle = %.2f" %Area)
print(" Perimeter of Equilateral Triangle = %.2f" %Perimeter)
print(" Semi Perimeter of Equilateral Triangle = %.2f" %Semi)
print(" Altitude of Equilateral Triangle = %.2f" %Altitude)




# Python Program to find Area of an Equilateral Triangle using Functions



import math

def Area_of_an_Equilateral_Triangle(side):
    # calculate the area
    Area = (math.sqrt(3)/ 4)*(side * side)
    
    # calculate the Perimeter
    Perimeter = 3 * side

    # calculate the semi-perimeter
    Semi = Perimeter / 2

    # calculate the Altitude
    Altitude = (math.sqrt(3)/2)* side

    print("\n Area of Equilateral Triangle = %.2f" %Area)
    print(" Perimeter of Equilateral Triangle = %.2f" %Perimeter)
    print(" Semi Perimeter of Equilateral Triangle = %.2f" %Semi)
    print(" Altitude of Equilateral Triangle = %.2f" %Altitude)