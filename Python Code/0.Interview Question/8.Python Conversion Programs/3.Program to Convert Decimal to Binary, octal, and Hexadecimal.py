'''
Program to Convert Decimal to Binary, octal, and Hexadecimal

'''


# Decimal to Binary, octal, and Hexadecimal
decimal = int(input("Please Enter the Decimal Number = "))

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print(decimal, " Decimal = ", binary, "Binary Value")
print(decimal, " Decimal = ", octal, "Octal Value")
print(decimal, " Decimal = ", hexadecimal, "Hexadecimal Value")