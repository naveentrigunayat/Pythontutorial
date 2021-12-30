

'''

Program to Print Inverted Right Triangle of Decreasing Order Numbers

'''




rows = int(input("Inverted Right Triangle Numbers in Decreasing Ord Rows = "))

print("==Inverted Right Triangle of Numbers in Decreasing Order Pattern==")

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = ' ')
    print()