'''

Program to Print Left Pascals Number Triangle

'''


rows = int(input("Enter Left Pascals Number Triangle Pattern Rows = "))

print("====Left Pascals Number Triangle Pattern====")

for i in range(1, rows + 1):
    for j in range(i, rows):
        print(end = '  ')
    for k in range(1, i + 1):
        print(k, end = ' ')
    print()

for i in range(rows, 0, -1):
    for j in range(i, rows + 1):
        print(end = '  ')
    for k in range(1, i):
        print(k, end = ' ')
    print()