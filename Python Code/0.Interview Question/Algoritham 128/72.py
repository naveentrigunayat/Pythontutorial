'''

Question:

Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.


Solution:



'''
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = round((low + high) / 2)
        
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
lst = [1,3,5,7,]
print(binary_search(lst, 9))   
