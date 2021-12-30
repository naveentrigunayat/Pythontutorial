'''

Program to check Triangle is Valid or Not

'''


# Python Program to check Triangle is Valid or Not




a = int(input('Please Enter the First Angle of a Triangle: '))
b = int(input('Please Enter the Second Angle of a Triangle: '))
c = int(input('Please Enter the Third Angle of a Triangle: '))

# checking Triangle is Valid or Not
total = a + b + c

if total == 180:
    print("\nThis is a Valid Triangle")
else:
    print("\nThis is an Invalid Triangle")




# Python Program to check Triangle is Valid or Not




a = int(input('Please Enter the First Angle of a Triangle: '))
b = int(input('Please Enter the Second Angle of a Triangle: '))
c = int(input('Please Enter the Third Angle of a Triangle: '))

# checking Triangle is Valid or Not
total = a + b + c

if (total == 180 and a != 0 and b != 0 and c != 0):
    print("\nThis is a Valid Triangle")
else:
    print("\nThis is an Invalid Triangle")