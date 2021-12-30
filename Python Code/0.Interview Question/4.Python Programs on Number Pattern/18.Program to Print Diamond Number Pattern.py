'''

Program to Print Diamond Number Pattern

'''


rows = int(input("Enter Diamond Number Pattern Rows = "))

print("====Diamond Number Pattern====")

for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end = ' ')
    for k in range(1, (2 * i)):
        print(k, end = '')
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, (rows - i + 1)):
        print(end = ' ')
    for k in range(1, (2 * i)):
        print(k, end = '')
    print()


# It is another way of writing a Python program to display the diamond pattern of numbers.

rows = int(input("Enter Diamond Number Pattern Rows = "))

print("====Diamond Number Pattern====") 
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end = ' ')
    for k in range(i, 0, -1):
        print(k, end = '')
    for l in range(2, i + 1):
        print(l, end = '')
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, (rows - i + 1)):
        print(end = ' ')
    for k in range(i, 0, -1):
        print(k, end = '')
    for l in range(2, i + 1):
        print(l, end = '')
    print()