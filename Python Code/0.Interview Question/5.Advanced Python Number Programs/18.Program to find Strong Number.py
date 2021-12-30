'''
Program to find Strong Number



Given a number ‘n’ we have to check whether the number given is Strong Number or not.

Strong number is a number whose sum of all digits’ factorial is equal to the number ‘n’. Factorial implies when we find the product of all the numbers below that number including that number and is denoted by ! (Exclamation sign), For example: 4! = 4x3x2x1 = 24.

So, to find a number whether its strong number, we have to pick every digit of the number like the number is 145 then we have to pick 1, 4 and 5 now we will find factorial of each number i.e, 1! = 1, 4! = 24, 5! = 120.

Now we will sum up 1 + 24 + 120 so we get 145, that is exactly same as the input given, So we can say that the number is strong number.

'''


Number = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Number

while(Temp > 0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1

    print("\n Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print("\n Sum of Factorials of a Given Number %d = %d" %(Number, Sum))
    
if (Sum == Number):
    print(" %d is a Strong Number" %Number)
else:
    print(" %d is not a Strong Number" %Number)