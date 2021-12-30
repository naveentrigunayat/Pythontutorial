'''
List Length

'''




# Python Length of an Empty List


emptyList = []
print("Length of a List = ", len(emptyList))


# Python Length of an Integer List


integerList = [12, 22, 33, 44, 55, 66, 77]
print("\n Original List = ", integerList)
      
print("Length of an Integer List = ", len(integerList))


# Python Length of a String List


stringList = ['Krishna', 'John', 'Yung', 'Ram', 'Steve']
print("\n Original List = ", stringList)
      
print("Length of a String List = ", len(stringList))


# Python Length of a String List


mixedList = ['Krishna', 20, 'John', 40.5, 'Yung', 11.98, 'Ram', 22]
print("\n Original List = ", mixedList)
      
print("Length of a Mixed List = ", len(mixedList))


# Python Length of a String List

mixedList = ['Krishna', 20, 'John', (40, 50, 65), 'Yung', 11.98, 'Ram']
print("\n Original List = ", mixedList)
      
print("Length of a Mixed List = ", len(mixedList))


# Python Length of a String List(nested List)

nestedList = ['Krishna', 20, 'John', [20, 40, 50, 65, 22], 'Yung', 11.98]
print("\n Original List = ", nestedList)
      
print("Length of a Nested List = ", len(nestedList[3]))



# Python List Length Example

intList = []
Number = int(input("Please enter the Total Number of Items in a List : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    intList.append(value)
    
print("\n Original List = ", intList)
      
print("Length of a Dynamic List = ", len(intList))