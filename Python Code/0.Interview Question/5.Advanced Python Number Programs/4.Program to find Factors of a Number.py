'''
Program to find Factors of a Number

Factors of a number are defined as numbers that divide the original number evenly or exactly. 
The meaning of factor is a whole number that can divide a greater number evenly. 

'''


def Find_Factors(number):
    for value in range(1, number + 1):
        if(number % value == 0):
            print("{0}".format(value))

num = int(input("Please Enter any Number: "))

print("Factors of a Given Number {0} are:".format(num))
Find_Factors(num)