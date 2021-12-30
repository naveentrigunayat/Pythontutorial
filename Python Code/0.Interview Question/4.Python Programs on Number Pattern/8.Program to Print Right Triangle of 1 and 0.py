'''
Program to Print Right Triangle of 1 and 0

'''


rows = int(input("Enter Right Triangle of 1 & 0 Num Pattern Rows = "))

print("====Right Angled Triangle of 1 and 0 Numbers Pattern====")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
           print(0, end = ' ') 
        else:
            print(1, end = ' ') 
    print()