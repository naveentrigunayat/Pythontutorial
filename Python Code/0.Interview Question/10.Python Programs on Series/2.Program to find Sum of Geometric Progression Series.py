'''
Program to find Sum of Geometric Progression Series

'''


'''
Python G.P. Series
Geometric Series is a sequence of elements in which the next item obtained by multiplying common ration to the previous item. 
Or G.P. Series is a series of numbers in which a common ratio of any consecutive numbers (items) is always the same.


The mathematical formula behind this Sum of G.P Series
Sn = a(rn) / (1- r)
Tn = ar(n-1)



'''


# Python Program to find Sum of Geometric Progression Series

import math

a = int(input("Please Enter First Number of an G.P Series: : "))
n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = (a * (1 - math.pow(r, n ))) / (1- r)
tn = a * (math.pow(r, n - 1))

print("\nThe Sum of Geometric Progression Series = " , total)
print("The tn Term of Geometric Progression Series = " , tn)



# Python Program to find Sum of Geometric Progression Series

a = int(input("Please Enter First Number of an G.P Series: : "))
n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = 0
value = a
print("\nG.P  Series :", end = " ")
for i in range(n):
    print("%d  " %value, end = " ")
    total = total + value
    value = value * r
    
print("\nThe Sum of Geometric Progression Series = " , total)



# Python Program to find Sum of Geometric Progression Series
import math

def sumofGP(a, n, r):
    total = (a * (1 - math.pow(r, n ))) / (1- r)
    return total

a = int(input("Please Enter First Number of an G.P Series: : "))
n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = sumofGP(a, n, r)
print("\nThe Sum of Geometric Progression Series = " , total)