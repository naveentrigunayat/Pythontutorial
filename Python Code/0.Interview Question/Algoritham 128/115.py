'''
Python Program to Find Product of Digits of given Number

'''


'''

Logic
First of all, we are declaring one variable product with value 1, we are going to use this variable to store the product of all digits, now after taking input from the user, inside the while loop, we have to extract each digit by performing modulo operation.

The modulo operation returns the remainder after dividing a number by another number. If we perform modulo operation with 10 on any number it will return the last most digit, we have to multiply and store the result into the variable product.

After that remove the last most digit from the number and perform the same again until the number becomes 0 or less than 0. Once the loop is completed simple print the variable product containing the product of all digit.


'''






# Take input from user
num = int(input("Enter any number : "))

temp = num
product = 1;

while(temp != 0):

    product = product * (temp % 10);

    # Remove last digit from temp.
    temp = int(temp / 10)

print("\nProduct of all digits in", num, ":", product)