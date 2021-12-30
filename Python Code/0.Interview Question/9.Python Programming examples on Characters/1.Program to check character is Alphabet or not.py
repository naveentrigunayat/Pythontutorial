'''
Program to check character is Alphabet or not

'''

# Python Program to check character is Alphabet or not



ch = input("Please Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is Not an Alphabet")





# Python Program to find character is Alphabet using isalpha functions





ch = input("Please Enter Your Own Character : ")

if(ch.isalpha()):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is Not an Alphabet")