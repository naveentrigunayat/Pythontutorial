'''
Program to find Rhombus Perimeter

'''


# Python Program to find Rhombus Perimeter




rhombusSide = float(input("Enter the Rhombus Side  = "))

rhombusPerimeter = 4 * rhombusSide

print("The Perimeter of a Rhombus = %.3f" %rhombusPerimeter) 



# Python Program to find Rhombus Perimeter




def calRhombusPerimeter(side):
    return 4 * side

rhombusSide = float(input("Enter the Rhombus Side  = "))

rhombusPerimeter = calRhombusPerimeter(rhombusSide)

print("The Perimeter of a Rhombus = %.3f" %rhombusPerimeter) 