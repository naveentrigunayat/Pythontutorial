'''
Program to Find Sum of Even and Odd Numbers in Tuple

'''

# Sum of Tuple Even and Odd Numbers

def sumOfEvenOddOddNumbers(evenOddTuple):
    tEvenSum = tOddSum = 0
    for eotup in evenOddTuple:
        if(eotup % 2 == 0):
            tEvenSum = tEvenSum + eotup
        else:
            tOddSum = tOddSum + eotup
    return tEvenSum, tOddSum

evenOddTuple = (10, 23, 20, 33, 43, 40, 60, 93, 120, 83) 
print("Even and Odd Tuple Items = ", evenOddTuple)

evenSum, oddSum = sumOfEvenOddOddNumbers(evenOddTuple)
print("The Sum of Even Numbers in evenOddTuple = ", evenSum)
print("The Sum of Odd  Numbers in evenOddTuple = ", oddSum)