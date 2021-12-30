'''
Program to Count Number of Digits in a Number 

'''


def Counting(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    return Count

Number = int(input("Please Enter any Number: "))
Count = Counting(Number)
print("\n Number of Digits in a Given Number = %d" %Count)