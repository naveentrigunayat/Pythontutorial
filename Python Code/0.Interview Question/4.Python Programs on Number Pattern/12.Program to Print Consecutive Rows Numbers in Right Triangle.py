'''
Program to Print Consecutive Rows Numbers in Right Triangle

'''


rows = int(input("Enter Consecutive Numbers in Right Triangle Pattern Rows = "))

print("====Consecutive Row Numbers Right Triangle Pattern====")

for i in range(1, rows + 1):
    val = i
    for j in range(1, i + 1):
        print(val, end = ' ')
        val = val + rows - j
    print()