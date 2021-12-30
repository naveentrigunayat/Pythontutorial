'''
Program to Count Occurrence of a Character in a String

'''


# Python Program to Count Occurrence of a Character in a String

def count_Occurrence(ch, str1):
    count = 0
    for i in range(len(string)):
        if(string[i] == char):
            count = count + 1
    return count

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

cnt = count_Occurrence(char, string)
print("The total Number of Times ", char, " has Occurred = " , cnt)