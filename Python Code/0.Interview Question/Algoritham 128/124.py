'''
Python Program To Count Vowels and Consonant in Given String in Python

'''

#                                 Programme 1


#Python program to count vowel or consonant of the given string
str=input("Please enter a string as you wish: ");
vowels=0
consonants=0

for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1;#vowel counter is incremented by 1
    else:
        consonants=consonants+1;
#consonant counter is incremented by 1
print("The number of vowels:",vowels);
print("\nThe number of consonant:",consonants);


#                                          programme 2


#Python program to count vowel or consonant of the given string
str=input("Please enter a string as you wish: ");
vowels=0
consonants=0
str.lower()#call the lower function to avoid upper case letter
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' ):
           vowels=vowels+1;
    else:
        consonants=consonants+1;
print("The number of vowels:",vowels);
print("\nThe number of consonant:",consonants);