'''
 program to Count Total Number of Words in a String

'''


# Python program to Count Total Number of Words in a String

def Count_Total_Words(str1):
    total = 1
    for i in range(len(str1)):
        if(str1[i] == ' ' or str1 == '\n' or str1 == '\t'):
            total = total + 1
    return total


string = input("Please Enter your Own String : ")
leng = Count_Total_Words(string)
print("Total Number of Words in this String = ", leng)