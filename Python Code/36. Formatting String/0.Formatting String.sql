#                                     Formatting String

C-Style String Formatting
format ( ) Method
f-String / Formatted String Literals


#                                C-Style String Formatting

% operator/ Modulo Operator/ Interpolation Operator – This operator is used for formatting strings. It interprets the left argument much like a sprintf( ) style format string to be applied to the right argument, and returns the string resulting from this formatting operation.
Syntax:- print(“format placeholder” %(data))
Format placeholder = %[flags][width][.precision]type
% - marks the start of the specifier
Flags – It affect the result of some conversion type
Width – Minimum field width
Precision – Given as . Followed by the precision
Type – Conversion type



Syntax:- print(“format placeholder” %(data))
Format placeholder = %[flags][width][.precision]type
data – It can be literal, variable, expression etc.
Ex:-

print(“My name is %s and My age is %d” % (“GeekyShows”, 62))



Maintain Order in above statement first string then integer


Syntax:- print(“format placeholder” % {‘key’:value})
Format placeholder = %(mapping_key)[flags][width][.precision]type
% - marks the start of the specifier
Mapping_key – Consisting of parenthesized sequence of characters
Flags – It affect the result of some conversion type
Width – Minimum field width
Precision – Given as . Followed by the precision
Type – Conversion type


Example:- 
print(“My name is %(nm)s and My age is %(ag)d” % {‘nm’:“GeekyShows”, ‘ag’:62})
print(“My name is %(nm)s and My age is %(ag)d” % {‘ag’:62, ‘nm’:“GeekyShows”})

Do not need to maintain Order in above statement.



#                                       C-Style String Formatting



Conversion Type                         Meaning

d                             Signed integer decimal.
I                             Signed integer Decimal
O                             Signed octal value.
x                             Signed hexadecimal (lowercase).
X                             Signed hexadecimal (uppercase).
e                             Floating point exponential format (lowercase).
E                             Floating point exponential format (uppercase).
f                             Floating point decimal format.
F                             Floating point decimal format.
g                  Floating Point format. Uses lower case exponential format if exponent is less than -4 or not less than precision, decimal format otherwise
G                  Floating Point format. Uses lower case exponential format if exponent is less than -4 or not less than precision, decimal format otherwise
c                  Single character (accepts integer or single character string)
r                  String (converts any python object using repr())
s                  String (converts any Python object using str()).
A                  String (Converts any python object using ascii())
%                  No argument is converted, result in a % character in the result



#                            C-Style String Formatting


Flag                     Meaning 


#             Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
0             The conversion will be zero padded for numeric values.
-             The converted value is left adjusted (overrides the '0' conversion if both are given).
              (a space) A blank should be left before a positive number (or empty string) produced by a signed conversion.
+             A sign character ('+' or '-') will precede the conversion (overrides a “space” flag).




#                               C-Style String Formatting


print(“%d” % 432)					432
print(“%d %d” % (432, 345))				432 345
print(“%f” % 432.123)				432.123000
print(“%f” % 432.123456)				432.123456
print(“%f” % 432.12345651)				432.123457
print(“%f” % 432.12345641)				432.123456
print("%s" % "GeekyShows")				GeekyShows
print("%s %s" % ("Hello", "GeekyShows"))		Hello GeekyShows
print("%d %s" % (432, "GeekyShows"))			432 GeekyShows
#print("%s %d" % (432, "GeekyShows")) 		TypeError
print(“%(nm)s  %(ag)d” % {‘ag’:432, ‘nm’:“GeekyShows”})  GeekyShows 432





