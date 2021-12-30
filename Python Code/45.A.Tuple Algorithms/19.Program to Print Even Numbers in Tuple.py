'''
Program to Print Even Numbers in Tuple

'''

# Tuple Even Numbers

def tupleEvenNumbers(evTuple):
    for tup in evTuple:
        if(tup % 2 == 0):
            print(tup, end = "  ")


evTuple = (19, 32, 25, 77, 44, 56, 89, 45, 98, 122, 55, 12) 
print("Tuple Items = ", evTuple)

print("\nThe Even Numbers in this evTuple Tuple are:")
tupleEvenNumbers(evTuple)