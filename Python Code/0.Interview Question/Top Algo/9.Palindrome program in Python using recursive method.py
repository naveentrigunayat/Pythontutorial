#                             Palindrome program in Python using recursive method


'''What is Palindrome Number?
A Palindrome number is a number which reverse is equal to the original number means number itself.

 

For example : 121, 111, 1223221, etc.

In the above example you can see that 121 is a palindrome number. Because reverse of the 121 is same as 121.'''


n = int(input("please give a number : "))

def reverse(num):
    if num<10:
      return num 
    else:
      return int(str(num%10) + str(reverse(num//10)))

def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(n) == 1:
    print("Given number is a palindrome")
else:
    print("Given number is a not palindrome") 