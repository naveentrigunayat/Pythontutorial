'''
Program to Print K Shape Number Pattern

'''

rows = int(input("Enter K Shape Number Pattern Rows = "))

print("====K Shape Number Pattern====")

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()

for i in range(2, rows + 1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()