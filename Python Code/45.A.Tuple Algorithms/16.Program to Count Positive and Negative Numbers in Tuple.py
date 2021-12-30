'''
Program to Count Positive and Negative Numbers in Tuple

'''


# Count of Tuple Positive and Negative Numbers

def CountOfPositiveNegativeNumbers(evodTuple):
    tPositiveCount = tNegativeCount = 0
    for pntup in evodTuple:
        if(pntup >= 0):
            tPositiveCount = tPositiveCount + 1
        else:
            tNegativeCount = tNegativeCount + 1
    return tPositiveCount, tNegativeCount

evodTuple = (26, -77, -99, 75, 14, -56, 19, 81, -1, 33) 
print("Positive and Negative Tuple Items = ", evodTuple)

PositiveCount, NegativeCount = CountOfPositiveNegativeNumbers(evodTuple)
print("The Count of Positive Numbers in evodTuple = ", PositiveCount)
print("The Count of Negative Numbers in evodTuple = ", NegativeCount)