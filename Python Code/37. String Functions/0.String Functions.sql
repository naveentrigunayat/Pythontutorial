#                                  String Functions


upper ( ) – This method is used to convert all character of a string into uppercase.
	Syntax:- string.upper( ) 

lower ( ) – This method is used to convert all character of a string into lowercase.
	Syntax:- string.lower( ) 

swapcase ( ) – This method is used to convert all lower case character into  uppercase and vice versa.
	Syntax:- string.swapcase ( ) 

title ( ) – This method is used to convert the string in such that each word in string will start with a capital letter and remaining will be small letter.
	Syntax:- string.title ( ) 



isupper ( ) – This method is used to test whether given string is in upper case or not, it returns True if string contains at least one letter and all characters are in upper case else returns False.
	Syntax:- string.isupper( )

islower ( ) – This method is used to test whether given string is in lower case or not, it returns True if string contains at least one letter and all characters are in lower case else returns False.
	Syntax:- string.islower( )

istitle ( ) – This method is used to test whether given string is in title format or not, it returns True if string contains at least one letter and each word of the string starts with a capital letter else returns False.
	Syntax:- string.istitle( )


isdigit ( ) – This method returns True if the string contains only numeric digits (0 to 9) else returns False.
	Syntax:- string.isdigit()

isalpha ( ) – This method returns True if the string has at least one character and all are alphabets ( A to Z and a to z) else returns False
	Syntax:- string.isalpha()

isalnum ( ) – This method returns True if the string has at least one character and all characters in the string are alphanumeric (A to Z, a to z and 0 to 9) else returns False
	Syntax:- string.isalnum()


isspace ( ) – This method returns True if the string contains only space else returns False.
	Syntax:- string.isspace()


lstrip ( ) – This method is used to remove the space which are at left side of the string.
	Syntax:- string.lstrip()

rstrip ( ) – This method is used to remove the space which are at right side of the string.
	Syntax:- string.rstrip()

strip ( ) – This method is used to remove the space from the both side of the string.
	Syntax:- string.strip()


replace ( ) – This method is used to replace a sub string in a string with another sub string.
	Syntax:- string.replace(old, new)

split ( ) – This method is used to split/break a string into pieces. These pieces returns as a list.
	Syntax:- string.split(‘separator’)

join ( ) – This method is used to join strings into one string.
	Syntax:- “separator”.join(string_list)


startswith ( ) – This method is used to check whether a string is starting with a substring or not. It returns True if the string starts with specified sub string.
	Syntax:- string.startswith(‘specified_string’)

endswith ( ) – This method is used to check whether a string is ending with a substring or not. It returns True if the string ends with specified sub string.
	Syntax:- string.startswith(‘specified_string’)
