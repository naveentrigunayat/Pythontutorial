#                          f-String / Formatted String Literal 


A formatted string literal or f-string is a string literal that is prefixed with f or F. 
These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.
Syntax:- f“{index/key/name:[fill][align][sign][#][0][width][,][.precision]type}”        <----- Format specification
Ex:- 
a = 10
print(f“{a}”)

Ex:- print(f“My age is {a}”)





Conversion Type                         Meaning

d                             Signed integer decimal.
I                             Signed integer Decimal
O                             Signed octal value.
x                             Signed hexadecimal (lowercase).
X                             Signed hexadecimal (uppercase).
e                             Floating point exponential format (lowercase).
E                             Floating point exponential format (uppercase).
f                             Floating point decimal format.(Default: 6)
F                             Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
c                             Character. Converts the integer to the corresponding Unicode character before printing
g                             General format. Rounds number to p significant digits. (Default precision: 6)
G                             Same as 'g'. Except switches to 'E' if the number is large.
n                             Same as 'd'. Except it uses current locale setting for number separator
s                             String (converts any Python object using str()).
%                             Percentage. Multiplies the number by 100 and displays in fixed ('f') format, followed by a percent sign.



#                                    Format Method


Alignment Type                    Meaning


<                         Forces the field to be left-aligned within the available space (This is default for most objects)
^                         Forces the field to be centered within the available space.
>                         Forces the field to be right-aligned within the available space (This is default for Numbers)
=                         Forces the padding to be placed after the sign (if any) but before the digits.
                           This is used for printing fields in the form ‘+000000120’.
                            This alignment option is only valid for numeric types.
                             It becomes the default when ‘0’ immediately precedes the field width.
+                         indicates that a sign should be used for both positive as well as negative numbers.
-                         indicates that a sign should be used only for negative numbers (this is the default behavior).
                          (a space) indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.





The '#' option causes the “alternate form” to be used for the conversion. The alternate form is defined differently for different types. This option is only valid for integer, float, complex and Decimal types. For integers, when binary, octal, or hexadecimal output is used, this option adds the prefix respective '0b', '0o', or '0x' to the output value.

The ',' option signals the use of a comma for a thousands separator. For a locale aware separator, use the 'n' integer presentation type instead.

The '_' option signals the use of an underscore for a thousands separator for floating point presentation types and for integer presentation type 'd'.



:[fill][align][sign][#][0][width][,][.precision]type


