'''
Program to Print a Simple Number Pattern

'''

rows = int(input("Enter Simple Numeber Pattern Rows = "))

print("====Printing Simple Number Pattern====")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print()


    