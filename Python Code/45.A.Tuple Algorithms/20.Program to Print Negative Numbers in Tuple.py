'''
Program to Print Negative Numbers in Tuple

'''

# Tuple Negative Numbers

def tupleNegativeNumbers(negTuple):
    for potup in negTuple:
        if(potup < 0):
            print(potup, end = "  ")


negTuple = (9, -23, -17, 98, 66, -12, -77, 0, -2, 15) 
print("Negative Tuple Items = ", negTuple)

print("\nThe Negative Numbers in negTuple Tuple are:")
tupleNegativeNumbers(negTuple)