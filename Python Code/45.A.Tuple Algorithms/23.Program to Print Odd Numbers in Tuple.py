'''
Program to Print Odd Numbers in Tuple

'''


# Tuple Odd Numbers

def tupleOddNumbers(oddTuple):
    for tup in oddTuple:
        if(tup % 2 != 0):
            print(tup, end = "  ")   # we use end to print line in single row with space


oddTuple = (122, 55, 12, 11, 67, 88, 42, 99, 17, 64) 
print("Tuple Items = ", oddTuple)

print("\nThe Odd Numbers in oddTuple Tuple are:")
tupleOddNumbers(oddTuple)