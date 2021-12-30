

'''
Program to Print Right Arrow Number Pattern
'''




rows = int(input("Enter Right Arrow Number Pattern Rows = "))

print("====Right Arrow Number Pattern====")

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j < i:
            print(end = '  ')
        else:
            print(j, end = ' ')      
    print()

for i in range(1, rows):
    for j in range(1, rows + 1):
        if j < rows - i:
            print(end = '  ')
        else:
            print(j, end = ' ')      
    print()