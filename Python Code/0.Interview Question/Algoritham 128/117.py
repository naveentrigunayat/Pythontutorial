'''
Python Program to Check a Number is Palindrome or Not

'''

'''

Problem Solution
1. Take the value of the integer and store in a variable.
2. Transfer the value of the integer into another temporary variable.
3. Using a while loop, get each digit of the number and store the reversed number in another variable.
4. Check if the reverse of the number is equal to the one in the temporary variable.
5. Print the final result.
6. Exit.

'''



n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")