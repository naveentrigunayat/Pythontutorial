'''
Program to Print Right Triangle of Incremented Numbers

'''


rows = int(input("Enter Right Triangle of Incremented Numbers Rows = "))

print("====Right Angled Triangle of Incremented Numbers Pattern====")

for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end = ' ') 
    print()