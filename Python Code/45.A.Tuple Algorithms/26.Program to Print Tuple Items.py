'''
Program to Print Tuple Items

'''


# Print Tuple Items

numTuple = (10, 20, 30, 40, 50)

print("The Tuple Items are ")
for i in range(len(numTuple)):
    print("Tuple Item at %d Position = %d" %(i, numTuple[i]))           

print("=========")
fruitsTuple = ('apple', 'orange', 'kiwi', 'grape')
for fruit in fruitsTuple:
    print(fruit)