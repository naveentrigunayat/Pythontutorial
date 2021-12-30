'''
Fibonacci Series program

The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it:

the 2 is found by adding the two numbers before it (1+1),
the 3 is found by adding the two numbers before it (1+2),
the 5 is (2+3),
and so on!


'''


# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))

# Initializing First and Second Values of a Series
First_Value = 0
Second_Value = 1
           
# Find & Displaying Fibonacci series
for Num in range(0, Number):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)