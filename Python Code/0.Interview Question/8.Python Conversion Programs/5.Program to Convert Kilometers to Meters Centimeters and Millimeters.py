'''
Program to Convert Kilometers to Meters Centimeters and Millimeters

'''


'''
Write a Python Program to Convert Kilometers to Meters, Centimeters, and Millimeters. 
This Python example allows inserting the kilometers and converts them to meters, millimeters, and centimeters. 
As we know, one kilometer equals 1000 meters, 100000 centimeters, and 1000000 millimeters.

'''


# Kilometers to Meter, Centimeter, and Millimeter

kilometers = float(input("Please Enter the Kilometers = "))

meter = kilometers * 1000
centimeter = kilometers * 100000
millimeter = kilometers * 1000000
 
print("%.2f Kilometers = %.2f Meters" %(kilometers, meter))
print("%.2f Kilometers = %.2f Centimeters" %(kilometers, centimeter))
print("%.2f Kilometers = %.2f Millimeters" %(kilometers, millimeter))