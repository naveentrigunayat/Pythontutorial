'''
 Program to find Area of a Trapezoid

'''


'''

Python Area of a Trapezoid
If we know the height and two base lengths then we can calculate the Area of a Trapezoid using the below formula:


Area = (a+b)/2 * h

Where a and b are the two bases and h is the height of the Trapezoid. And, we can calculate the median of a Trapezoid using the following formula:

Median = (a+b) / 2.


If we know the Median and height then we can calculate the Area of a Trapezoid as: median * height

'''


'''
Program to find Area of a Trapezoid
This python program allows the user to enter both sides of the Trapezoid and height. 
Using those values, this Python program will calculate the Area of a trapezoid and Median of a Trapezoid.

'''


# Python Program to find Area of a Trapezoid

base1 = float(input('Please Enter the First Base of a Trapezoid: '))
base2 = float(input('Please Enter the Second Base of a Trapezoid: '))
height = float(input('Please Enter the Height of a Trapezoid: '))

# calculate the area
Area = 0.5 * (base1 + base2) * height

# calculate the Median
Median = 0.5 * (base1+ base2)

print("\n Area of a Trapezium = %.2f " %Area)
print(" Median of a Trapezium = %.2f " %Median)




# Python Program to find Area of a Trapezoid using Functions




def Area_of_a_Trapezoid (base1, base2, height):
    # calculate the area
    Area = 0.5 * (base1 + base2) * height

    # calculate the Median
    Median = 0.5 * (base1+ base2)

    print("\n Area of a Trapezium = %.2f " %Area)
    print(" Median of a Trapezium = %.2f " %Median)

Area_of_a_Trapezoid (9, 6, 4)