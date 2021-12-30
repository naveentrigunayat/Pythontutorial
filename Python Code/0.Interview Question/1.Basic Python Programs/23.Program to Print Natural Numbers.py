'''
Program to Print Natural Numbers

'''


minimum = int(input("Please Enter the Minimum integer Value : "))
maximum = int(input("Please Enter the Maximum integer Value : "))

print("The List of Natural Numbers from {0} to {1} are".format(minimum, maximum)) 

for i in range(minimum, maximum + 1):
    print (i, end = '  ')