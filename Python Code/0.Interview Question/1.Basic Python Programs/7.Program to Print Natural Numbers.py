'''
Program to Print Natural Numbers


Natural Numbers : the positive integers (whole numbers) 1, 2, 3, etc., and sometimes zero as well.
'''


minimum = int(input("Please Enter the Minimum integer Value : "))
maximum = int(input("Please Enter the Maximum integer Value : "))

print("The List of Natural Numbers from {0} to {1} are".format(minimum, maximum)) 

for i in range(minimum, maximum + 1):
    print (i, end = '  ')