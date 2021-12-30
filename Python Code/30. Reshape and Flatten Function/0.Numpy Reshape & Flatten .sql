#                                           reshape ( ) Function



This function is used to change the shape of array. We can convert 1D array to 2D or 3D array and vice versa. The new array should have the same number of elements as in the original array.
Syntax:- 
reshape(array_name, (n, r, c))
Where, 
array_name – It represents the name of the array whose elements to be converted.
n – n is the number of arrays in the resultant array
r – r is the number of rows
c – c is the number of columns 



#                                         Convert 1D Array to 2D Array


a = array([1, 2, 3, 4, 5, 6])
b = reshape(a, (2, 3))


b = [  [1, 2, 3] 
         [4, 5, 6]   ]



#                                        Convert 1D Array to 3D Array


c = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
d = reshape(c, (2, 3, 2))


d = [ [ [1, 2], 
           [3, 4],
           [5, 6] ],  
         [ [7, 8],
           [9, 10],
           [11, 12] ]  ]



#                                            Convert 2D Array to 1D Array


e = array([[1, 2, 3], [4, 5, 6]])
f = reshape(e, (6))
f = [1, 2, 3, 4, 5, 6]




#                                      flatten ( ) Method


The flatten ( ) method is used to convert 2D or 3D array to 1D array.
Syntax:- array_name.flatten()
Ex-
e = array([[1, 2, 3], [4, 5, 6]])
f = e.flatten()


