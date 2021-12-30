'''
Python | Largest, Smallest, Second Largest, Second Smallest in a List

'''


# Python program to find largest, smallest,
# second largest and second smallest in a
# list with complexity O(n)
def Range(list1):
	largest = list1[0]
	lowest = list1[0]
	largest2 = None
	lowest2 = None
	for item in list1[1:]:	
		if item > largest:
			largest2 = largest
			largest = item
		elif largest2 == None or largest2 < item:
			largest2 = item
		if item < lowest:
			lowest2 = lowest
			lowest = item
		elif lowest2 == None or lowest2 > item:
			lowest2 = item
			
	print("Largest element is:", largest)
	print("Smallest element is:", lowest)
	print("Second Largest element is:", largest2)
	print("Second Smallest element is:", lowest2)


# Driver Code
list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
Range(list1)
