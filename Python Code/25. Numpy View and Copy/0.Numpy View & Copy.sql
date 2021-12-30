#                                        view ( ) Method


view ( ) – This method is used to construct a new view of array with same data of existing array. The existing array and new array will share different memory locations. 
If the new array get modified, the existing will also be modified as the elements in both the arrays will be like mirror image. 
Ex:-
a = array([10, 20, 30, 40, 50])
b = a.view( )



#                                         copy ( ) Method


copy ( ) – This method is used to create a copy of an existing array. If the new array get modified, the existing array will not be affected or vice versa. Both the arrays are independent.
Ex:-
a = array([10, 20, 30, 40, 50])
b = copy(a)



