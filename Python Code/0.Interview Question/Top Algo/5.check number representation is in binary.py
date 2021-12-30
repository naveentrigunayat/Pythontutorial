#                         check number representation is in binary


'''
How our program will behave?
In the below program if someone give any input in 0 and 1 format then our program will run and give output as given number is in binary format.

And if someone give another number different from 0 and 1 like 2, 3 or any other then our program will give output as given number is not in a binary format.
'''
num = int(input("please give a number : "))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
        print("num is not binary")
        break
    num=num//10
    if num==0:
        print("num is binary") 