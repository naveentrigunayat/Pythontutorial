'''
 Program to check character is Alphabet or Digit

'''


ch = input("Please Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Given Character ", ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not an Alphabet or a Digit")




#  Program to find character is Alphabet or Digit using isalpha, isdigit functions



ch = input("Please Enter Your Own Character : ")

if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
elif(ch.isalpha()):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is Not an Alphabet or a Digit")