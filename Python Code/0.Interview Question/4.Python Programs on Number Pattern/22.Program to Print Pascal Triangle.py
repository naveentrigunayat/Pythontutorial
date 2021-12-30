'''
Program to Print Pascal Triangle

'''


from math import factorial

rows = int(input("Enter Pascals Triangle Number Pattern Rows = "))

print("====Pascals Triangle Number Pattern====")

for i in range(0, rows):
    for j in range(rows - i + 1):
        print(end = ' ')
    for k in range(0, i + 1):
        print(factorial(i)//(factorial(k) * factorial(i - k)), end = ' ')
    print()



