'''
Calculate Square of a Number

'''


def square(num):
    return num * num

number = float(input(" Please Enter any numeric Value : "))

sqre = square(number)

print("The Square of a Given Number {0}  = {1}".format(number, sqre))