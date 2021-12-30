#                                     count occurrence of characters in string

'''
How this Python program will behave?
This Python program will take a string and a character as an input. And it will count the  occurrence of a given character. This program will also count spaces I we will give it.

For example:
If we have given a String as an input “Quescol is educational website” and also a character ‘s’.

Then after counting character ‘a’, program will return output 2.'''


string = input("Please enter String : ")
char = input("Please enter a Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("Total Number of occurence of ", char, "is :" , count)