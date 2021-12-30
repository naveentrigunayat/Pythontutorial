'''
Program to Convert Centimeters to Meters and Kilometers

'''

# Centimeter to Meters and Kilometers



centimeter = float(input("Please Enter the Centimeters = "))

meter = centimeter/100
kilometers = centimeter/100000
 
print("%.2f Centimeters = %.2f Meters" %(centimeter, meter))
print("%.2f Centimeters = %.2f Kilometers" %(centimeter, kilometers)) 