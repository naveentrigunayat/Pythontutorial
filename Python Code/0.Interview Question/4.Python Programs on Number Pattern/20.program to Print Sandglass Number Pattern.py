'''
program to Print Sandglass Number Pattern

'''


rows = int(input("Enter Sandglass Number Pattern Rows = "))

print("====Sandglass Number Pattern====")

for i in range(1, rows + 1):
    for j in range(1, i):
        print(end = ' ')
    for k in range(i, rows + 1):
        print(k, end = ' ')                
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, i):
        print(end = ' ')
    for k in range(i, rows + 1):
        print(k, end = ' ')      
    print()