'''
Program to Check Leap


Leap Year :  February 29 is a date that usually occurs every four years, and is called the leap day. 
This day is added to the calendar in leap years
'''


year = int(input("Please Enter the Year Number you wish: "))

if (year%400 == 0):
          print("%d is a Leap Year" %year)
elif (year%100 == 0):
          print("%d is Not the Leap Year" %year)
elif (year%4 == 0):
          print("%d is a Leap Year" %year)
else:
          print("%d is Not the Leap Year" %year)