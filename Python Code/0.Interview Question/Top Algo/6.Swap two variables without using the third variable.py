#                              Swap two variables without using the third variable


'''How our program will behave?
As we already seen above that what we have to achieve in the program.

In the swapping program without using third variable we will assign two different value to the different variables.

 

For example: a=2 and b=4

 

Now after execution of the program our output should like 

a=4 and b = 2'''


a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b);