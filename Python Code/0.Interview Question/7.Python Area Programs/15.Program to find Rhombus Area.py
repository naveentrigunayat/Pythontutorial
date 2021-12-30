'''
Program to find Rhombus Area

'''



# Python Program to find Rhombus Area




rhombusD1 = float(input("Enter Rhombus First Diagonal  = "))

rhombusD2 = float(input("Enter Rhombus Second Diagonal = "))

rhombusArea = (rhombusD1 * rhombusD2)/2

print("The Area of a Rhombus = %.3f" %rhombusArea) 



# Python Program to find Rhombus Area




def calRhombusArea(d1, d2):
    return (d1 * d2)/2

rhombusD1 = float(input("Enter Rhombus First Diagonal  = "))

rhombusD2 = float(input("Enter Rhombus Second Diagonal = "))

rhombusArea = calRhombusArea(rhombusD1, rhombusD2)

print("The Area of a Rhombus = %.3f" %rhombusArea) 