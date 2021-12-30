'''
Program to Print Inverted Right Triangle Numbers in Reverse

'''



rows = int(input("Inverted Right Triangle Numbers in Reverse pattern Rows = "))

print("==Inverted Right Triangle of Numbers in Reverse Order Pattern==")

for i in range(1, rows + 1):
    for j in range(rows, i - 1, -1):
        print(j, end = ' ')
    print()