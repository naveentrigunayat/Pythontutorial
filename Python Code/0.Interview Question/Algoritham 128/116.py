'''

Python Program to Reverse of a Number 

'''


# Using Function


def reverse(n):
    rev = 0

    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = int(n / 10)
    return rev


x = int(input("Enter a number:"))
result = reverse(x)
print("Reverse is:", result)



# Using Recursion

num = int(input("Enter the number: "))  
revr_num = 0    # initial value is 0. It will hold the reversed number  
def recur_reverse(num):  
    global revr_num   # We can use it out of the function  
    if (num > 0):  
        Reminder = num % 10  
        revr_num = (revr_num * 10) + Reminder  
        recur_reverse(num // 10)  
    return revr_num  
  
  
revr_num = recur_reverse(num)  
print("n Reverse of entered number is = %d" % revr_num)  