'''
Program to Print Positive Numbers in Tuple

'''


# Tuple Positive Numbers

def tuplePositiveNumbers(posTuple):
    for potup in posTuple:
        if(potup >= 0):
            print(potup, end = "  ")


posTuple = (19, -32, -17, 98, 44, -12, 0, 78, -2, 4, -5) 
print("Positive Tuple Items = ", posTuple)

print("\nThe Positive Numbers in this posTuple Tuple are:")
tuplePositiveNumbers(posTuple)