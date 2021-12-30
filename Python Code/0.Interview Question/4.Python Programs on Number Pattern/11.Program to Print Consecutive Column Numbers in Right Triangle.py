'''
Program to Print Consecutive Column Numbers in Right Triangle

'''


rows = int(input("Enter Consecutive Col Nums Right Triangle Pattern Rows = "))

print("====Consecutive Column Numbers Right Triangle Pattern====")
val = 0

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        val = val + 1
        print(val, end = ' ')
    print()



