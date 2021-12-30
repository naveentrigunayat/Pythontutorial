'''
Program to find Parallelogram Area

'''


'''
Write a Python Program to find the Parallelogram Area.
 This Python example allows entering parallelogram base and height and finds the area by multiplying both.

'''

# Python Program to find Parallelogram Area



parallelBase = float(input("Enter Parallelogram Base : "))

ParallelHeight = float(input("Enter Parallelogram Height : "))

parallelArea = parallelBase * ParallelHeight

print("The Area of a Parallelogram = %.3f" %parallelArea) 




# Python Program to find Parallelogram Area




def calParallelogramArea(a, b):
    return a * b;

parallelBase = float(input("Enter Parallelogram Base : "))

ParallelHeight = float(input("Enter Parallelogram Height : "))

parallelArea = calParallelogramArea(parallelBase, ParallelHeight)

print("The Area of a Parallelogram = %.3f" %parallelArea) 