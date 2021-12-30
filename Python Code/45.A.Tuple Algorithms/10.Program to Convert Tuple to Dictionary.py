'''
Program to Convert Tuple to Dictionary

'''


# Convert Tuple to Dictionary

tup = ((1, 'USA'), (2, 'UK'), (3, 'France'), (4, 'Germany'))
print(tup)

tupToDict1 = dict(map(reversed, tup))
print(tupToDict1)
print()

tupToDict2 = dict(i[::1] for i in tup)
print(tupToDict2)
print()

tupToDict3 = dict(i[::-1] for i in tup)
print(tupToDict3)