
'''

Armstrong Number

A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.

For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.

'''



# Python Program For Armstrong Number using Functions

def Armstrong_Number(Number):
           # Initializing Sum and Number of Digits
           Sum = 0
           Times = 0

           # Calculating Number of individual digits
           Temp = Number
           while Temp > 0:
                      Times = Times + 1
                      Temp = Temp // 10

           # Finding Armstrong Number
           Temp = Number
           for n in range(1, Temp + 1):
                      Reminder = Temp % 10
                      Sum = Sum + (Reminder ** Times)
                      Temp //= 10
           return Sum
#End of Function

#User Input
Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

if (Number == Armstrong_Number(Number)):
    print("\n %d is Armstrong Number.\n" %Number)
else:
    print("\n %d is Not a Armstrong Number.\n" %Number)





# Python Program For Armstrong Number using Recursion

# Initializing Number of Digits
Sum = 0
Times = 0

# Calculating Number of individual digits
def Count_Of_Digits(Number):
           global Times
           if(Number > 0):
                      Times = Times + 1
                      Count_Of_Digits(Number // 10)
           return Times
#End of Count Of Digits Function

# Finding Armstrong Number
def Armstrong_Number(Number, Times):
           global Sum
           if(Number > 0):
                      Reminder = Number % 10
                      Sum = Sum + (Reminder ** Times)
                      Armstrong_Number(Number //10, Times)
           return Sum
#End of Armstrong Function

#User Input
Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

Times = Count_Of_Digits(Number)
Sum = Armstrong_Number(Number, Times)
if (Number == Sum):
    print("\n %d is Armstrong Number.\n" %Number)
else:
    print("\n %d is Not a Armstrong Number.\n" %Number)