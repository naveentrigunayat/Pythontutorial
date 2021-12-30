
'''

Python Program to Display Right Angled Triangle Star Pattern

'''




rows = int(input("Please Enter the Total Number of Rows  : "))   # Number Of Rows Required
ch = input("Please Enter any Character  : ")      # Character For Print

print("Right Angled Triangle Star Pattern") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('%c' %ch, end = '  ')
    print()



