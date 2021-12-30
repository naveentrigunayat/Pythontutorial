'''
Program to Print Inverted Right Triangle of Consecutive Numbers

'''


rows = int(input("Inverted Right Triangle Consecutive Row Numbers Rows = "))

print("==Inverted Right Triangle Consecutive Rows Numbers Pattern==")

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()