'''
Program to find Sum of N Natural Numbers

'''


def sum_of_n_natural_numbers(num):
    if(num == 0):
        return num
    else:
        return (num * (num + 1) / 2)
    
number = int(input("Please Enter any Number: "))

total_value = sum_of_n_natural_numbers(number)

print("Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total_value))