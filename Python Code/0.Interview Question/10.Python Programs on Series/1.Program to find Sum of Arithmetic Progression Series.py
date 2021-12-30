'''
Program to find Sum of Arithmetic Progression Series

'''

'''
Python A.P. Series
Arithmetic Series is a sequence of terms in which the next item obtained by adding a common difference to the previous item. Or A.P. series is a series of numbers in which the difference of any two consecutive numbers is always the same. This difference called a common difference.


In Mathematical behind calculating Arithmetic Progression Series
Sum of A.P. Series : Sn = n/2(2a + (n – 1) d)
Tn term of A.P. Series: Tn = a + (n – 1) d

'''


# Python Program to find Sum of Arithmetic Progression Series

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("\nThe Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)



# Python Program to find Sum of Arithmetic Progression Series

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d
i = a
print("\nThe tn Term of Arithmetic Progression Series = " , tn)
print("The Sum of Arithmetic Progression Series : ")
while(i <= tn):
    if(i != tn):
        print("%d + " %i, end = " ")
    else:
        print("%d = %d" %(i, total))
    i = i + d




# Python Program to find Sum of Arithmetic Progression Series

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = 0
value = a
print("Arithmetic Progression Series : ", end = " ")
for i in range(n):
    print("%d + " %value, end = " ")
    total = total + value
    value = value + d

print("\nThe Sum of Arithmetic Progression Series upto %d = %d " %(n, total))