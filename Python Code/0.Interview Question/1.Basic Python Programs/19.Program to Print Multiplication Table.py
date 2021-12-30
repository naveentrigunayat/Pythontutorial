'''
Program to Print Multiplication Table

'''


print(" Multiplication Table ")

for i in range(8, 10):
    for j in range(1, 11):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
    print('==============')