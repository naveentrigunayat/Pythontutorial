#      Python program to reverse a number with explanation


'''Suppose if someone gives input 123 and our program should give output 321.

Logic behind it is, first our target is to take last number and store it and then second last and append it with previous one and then rest.'''

'''Input Integer:  number  
(1) Initialize variable revs_number = 0  
(2) Loop while number > 0  
     (a) Multiply revs_number by 10 and add remainder of number   
          divide by 10 to revs_number  
               revs_number = revs_number*10 + number%10;  
     (b) Divide num by 10  
(3) Return revs_number  '''



# Ask for enter the number from the use  
number = int(input("Enter the integer number: "))  
  
# Initiate value to null  
revs_number = 0  
  
# reverse the integer number using the while loop  
  
while (number > 0):  
    # Logic  
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
  
# Display the result  
print("The reverse number is : {}".format(revs_number))  