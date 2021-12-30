'''
Program to Count Even and Odd Numbers in Tuple

'''

# Count of Tuple Even and Odd Numbers

def CountOfEvenOddOddNumbers(evodTuple):
    tEvenCount = tOddCount = 0
    for oetup in evodTuple:
        if(oetup % 2 == 0):
            tEvenCount = tEvenCount + 1
        else:
            tOddCount = tOddCount + 1
    return tEvenCount, tOddCount

evodTuple = (12, 26, 77, 99, 66, 75, 14, 256, 19, 81, 11, 33) 
print("Even and Odd Tuple Items = ", evodTuple)

evenCount, oddCount = CountOfEvenOddOddNumbers(evodTuple)
print("The Count of Even Numbers in evodTuple = ", evenCount)
print("The Count of Odd  Numbers in evodTuple = ", oddCount)