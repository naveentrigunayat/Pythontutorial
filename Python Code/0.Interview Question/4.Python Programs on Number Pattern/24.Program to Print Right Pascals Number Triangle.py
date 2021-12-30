'''
Program to Print Right Pascals Number Triangle

'''


rows = int(input("Enter Right Pascals Number Triangle Pattern Rows = "))

print("====Right Pascals Number Triangle Pattern====")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()



    