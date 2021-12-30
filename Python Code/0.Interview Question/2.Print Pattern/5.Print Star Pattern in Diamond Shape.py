'''
5.Print Star Pattern in Diamond Shape

'''

# OutPut Not Matching 

def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'*'*(i+1))
    for j in range(rows-1,0,-1):
        print(' '*(rows-j)+'*'*(j))

n = int(input("Enter the Number of Rows : "))
pyramid(n)