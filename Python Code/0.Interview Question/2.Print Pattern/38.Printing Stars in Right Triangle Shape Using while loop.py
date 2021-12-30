'''
38. Printing Stars in Right Triangle Shape Using while loop

'''


num = int(input("Enter the Number Of Rows : "))

row = 0

while row<num:
    star = row + 1
    while star > 0:
        print("*",end="")
        star = star - 1
    row = row + 1
    print()