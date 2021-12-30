'''
Program to check character is Lowercase or Uppercase

'''


# Python Program to check character is Lowercase or Uppercase using islower and isupper functions


ch = input("Please Enter Your Own Character : ")

if(ch.isupper()):
    print("The Given Character ", ch, "is an Uppercase Alphabet")
elif(ch.islower()):
    print("The Given Character ", ch, "is a Lowercase Alphabet")
else:
    print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")





# Python Program to check character is Lowercase or Uppercase




ch = input("Please Enter Your Own Character : ")

if(ch >= 'A' and ch <= 'Z'):
    print("The Given Character ", ch, "is an Uppercase Alphabet") 
elif(ch >= 'a' and ch <= 'z'):
    print("The Given Character ", ch, "is a Lowercase Alphabet")
else:
    print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")
