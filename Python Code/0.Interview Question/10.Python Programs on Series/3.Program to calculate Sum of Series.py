'''
Program to calculate Sum of Series 1²+2²+3²+….+n²

'''




# Python Program to calculate Sum of Series 1²+2²+3²+….+n²
 
number = int(input("Please Enter any Positive Number  : "))
total = 0

total = (number * (number + 1) * (2 * number + 1)) / 6

for i in range(1, number + 1):
    if(i != number):
        print("%d^2 + " %i, end = ' ')
    else:
        print("{0}^2 = {1}".format(i, total))



# Python Program to calculate Sum of Series 1²+2²+3²+….+n²
 
def sum_of_square_series(number):
    total = 0

    total = (number * (number + 1) * (2 * number + 1)) / 6

    for i in range(1, number + 1):
        if(i != number):
            print("%d^2 + " %i, end = ' ')
        else:
            print("{0}^2 = {1}".format(i, total))


num = int(input("Please Enter any Positive Number  : "))
sum_of_square_series(num)



# Python Program to calculate Sum of Series 1²+2²+3²+….+n²
 
def sum_of_square_series(number):
    if(number == 0):
        return 0
    else:
        return (number * number) + sum_of_square_series(number - 1)


num = int(input("Please Enter any Positive Number  : "))
total = sum_of_square_series(num)

print("The Sum of Series upto {0}  = {1}".format(num, total))