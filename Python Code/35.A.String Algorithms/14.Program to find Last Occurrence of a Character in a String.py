'''
Program to find Last Occurrence of a Character in a String

'''



# Python Program to find Last Occurrence of a Character in a String

def last_Occurrence(char, string):
    index = -1
    for i in range(len(string)):
        if(string[i] == char):
            index = i
    return index

str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")

flag = last_Occurrence(ch, str1)

if(flag == -1):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The Last Occurrence of ", ch, " is Found at Position " , flag + 1)