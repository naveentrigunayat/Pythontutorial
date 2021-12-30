'''
Python Program to find Sum of Cube of Digits of a Given Number

'''

# Method 1: Using a loop :

def findCubeSum(n):
    sum = 0
    for value in range(1, n+1):
        sum += value**3
    return sum


n = int(input("Enter the value of n : "))

print("Cube sum : ", findCubeSum(n))


#        Method 2: Recursive approach :


def findCubeSum(n):
    if(n<=1):
        return 1;
    return n**3 + findCubeSum(n-1)


n = int(input("Enter the value of n : "))

print("Cube sum : ", findCubeSum(n))