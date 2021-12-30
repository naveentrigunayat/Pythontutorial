#                                  String


String – String represents group of characters. Strings are enclosed in double quotes or single quotes. The str data type represents a String.
Ex:- “Hello”, “GeekyShows”, ‘Rahul’
str1 = “GeekyShows”


#                               Creating String


Single Quotes
str1 = ‘GeekyShows’

Double quotes
str2 = “GeekyShows”

Triple Single Quotes – This is useful to create strings which span into several lines. 
str3 = ‘‘‘ Hello Guys
               Please Subscribe
               Geekyshows’’’

Triple Double Quotes – This is useful to create strings which span into several lines. 
str4 = “““Hello Guys
                 Please Subscribe
                 Geekyshows ”””



Double Quote inside Single Quotes
str5 = ‘Hello “Geeky Shows” How are you’

Single Quote inside Double quotes
str6 = “Hello ‘Geeky Shows’ How are you”

Using Escape Characters
str7 = “Hello \nHow are You ?”

Raw String – Row string is used to nullify the effect of escape characters.
str8 = r“Hello \nHow are You ?”



#                               Memory Allocation



str1 = “GeekyShows”

str2 = “GeekyShows”

str3 = “Python”


#                              Index


Index represents the position number of characters in a string.
Ex:- 
str1 = “GeekyShows”

            
                                   -2 -1
            G  e  e  k  y  S  h  o  w  s
            0  1  2


#                                Accessing Character and String

str1 = “GeekyShows”

print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[-1])

print(str1)



#                                   String Length


Length of string represents the number of characters in a string.
len( ) Function is used to get length of string.
Ex:- 
str1 = “GeekyShows”
n = len(str1)



#                         Access using Loop

str1 = “GeekyShows”
for c in str1:
       print(c)

for i range(len(str1)):
       print(str1[i])

i = 0
while i < len(str1) :
       print(str1[i])
       i+=1


#                            Mutable and Immutable Object

Mutable Object – Mutable objects are those object whose value or content can be changed as and when required.
	Ex:- List, Set, Dictionaries 

Immutable Object – Immutable objects are those object whose value or content can not be changed.
	Ex:- Numbers, String, Tuple



#                 Immutable String


In Python, Strings are immutable object which means it’s value or content can not be changed.
str1 = “GeekyShows”



str1[4] =“i”
TypeError



#                      Slicing String


Slicing on String can be used to retrieve a piece of the string. Slicing is useful to retrieve a range of elements. 
Syntax:- 
new_string_name = string_name[start:stop:stepsize]
start – It represents starting point. By default its 0
stop – It represents ending point.
stepsize – It represents step interval. By default It is 1
If start and stop are not specified then slicing is done from 0th to n-1th  elements.
Start and Stop can be negative number.


#                      Repetition Operator

Repetition operator is used to repeat the string for several times. It is denoted by *
Ex:- 
“$” * 7

str1 = “Geeky Shows ”
str1 * 5


#                           Concatenation Operator


Concatenation operator is used to join two string. It is denoted by +
Ex:-
“Geeky” + “Shows”

str1 = “Geeky ”
str2 = “Shows”
str1 + str2


#                             Comparing String


str1 = “GeekyShows”
str2 = “GeekyShows”
result = str1 == str2

str1 = “GeekyShows”
str2 = “Python”
result = str1 == str2

str1 = “A”
str2 = “B”
result = str1 < str2



Operators                   Meaning

<                         Less than
>                         Greater Than 
<=                        Less Than or Equal to
>=                        Greater than or Equal to
==                        Equal to 
!=                        Not Equal to

