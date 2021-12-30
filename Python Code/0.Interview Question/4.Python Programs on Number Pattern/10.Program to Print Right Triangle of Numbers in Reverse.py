'''
Program to Print Right Triangle of Numbers in Reverse

'''


rows = int(input("Right Triangle Reverse Numbers Rows = "))

print("==Right Triangle of Numbers in Reverse Order Pattern==")

for i in range(rows, 0, -1):
    for j in range(rows, i - 1, -1):
        print(j, end = ' ')
    print()