'''
Print Pyramid Star Pattern in Reverse patten

'''


num = int(input("enter the number :"))

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()