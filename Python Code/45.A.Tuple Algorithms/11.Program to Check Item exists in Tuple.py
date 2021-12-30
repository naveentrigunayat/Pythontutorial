'''
Program to Check Item exists in Tuple

'''

# Check Element Presnet in Tuple

numTuple = (4, 6, 8, 11, 22, 43, 58, 99, 16)
print("Tuple Items = ", numTuple)

number = int(input("Enter Tuple Item to Find = "))

result = False

for val in numTuple:
    if val == number:
        result = True
        break

print("Does our numTuple Contains the ", number, "? ", result)