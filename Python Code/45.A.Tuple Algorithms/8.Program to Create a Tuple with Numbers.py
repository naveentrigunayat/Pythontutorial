'''
Program to Create a Tuple with Numbers

'''

# Create a Numeric Tuple

intTuple = ()
number = int(input("Please enter the Total Tuple Items to store = "))
for i in range(1, number + 1):
    value = int(input("Please enter %d Tuple Item = " %i))
    intTuple += (value,)

print("Tuple Items = ", intTuple)


