'''
Program to Print Same Numbers on all Sides of a Square

'''

rows = int(input("Enter Square of same Numbers Pattern Rows = "))

print("====Print Same Numbers on all Sides of a Square Pattern====")

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i < j:
            print(rows - i + 1, end = ' ')
        else:
            print(rows - j + 1, end = ' ')
    for k in range(rows - 1, 0, - 1):
        if i < k:
            print(rows - i + 1, end = ' ')
        else:
            print(rows - k + 1, end = ' ')
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, rows + 1):
        if i < j:
            print(rows - i + 1, end = ' ')
        else:
            print(rows - j + 1, end = ' ')
    for k in range(rows - 1, 0, - 1):
        if i < k:
            print(rows - i + 1, end = ' ')
        else:
            print(rows - k + 1, end = ' ')
    print()