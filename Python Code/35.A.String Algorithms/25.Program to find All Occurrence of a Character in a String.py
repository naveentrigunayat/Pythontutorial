'''
Program to find All Occurrence of a Character in a String

'''


# Python Program to find Occurrence of a Character in a String

def all_Occurrence(ch, str1):
    for i in range(len(str1)):
        if(str1[i] == ch ):
            print(ch, " is Found at Position " , i + 1)

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
all_Occurrence(char, string)