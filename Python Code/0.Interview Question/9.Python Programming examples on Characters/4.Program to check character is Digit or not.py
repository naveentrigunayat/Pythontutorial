'''
Program to check character is Digit or not

'''


# Python Program to check character is Digit or not



ch = input("Please Enter Your Own Character : ")

if(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not a Digit")




# Program to verify character is Digit using isdigit functions


ch = input("Please Enter Your Own Character : ")

if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not a Digit")