#                                              Set Type


A set is an unordered collection of elements much like a set in mathematics. 
The order of elements is not maintained in the sets. It means the elements may not appear in the same order as they are entered into the set. 
A set does not accept duplicate elements. 
Set is mutable so we can modify it.
Sets are unordered so we can not access its element using index.
Sets are represented using curly brackets { }
a = {10, 20, 30, “GeekyShows”, “Raj”, 40}
 


#                                      Creating a Set


A set is created by placing all the items (elements) inside curly braces {}, separated by comma. A set does not accept duplicate elements. 
Elements can be of different types except mutable element, like list, set or dictionary.
Ex:- 
a = {10, 20, 30}
a = {10, 20, 30, “GeekyShows”, “Raj”, 40}
a = {10, 20, 30, “GeekyShows”, “Raj”, 40, 10, 20}



#                                  Creating Empty Set


We can create an empty set using set( ) function. 
a = set()



#                              Accessing elements


Sets are unordered so we can not access its element using index.
a = {10, 20, “GeekyShows”, “Raj”, 40}
a[0]
print(a)



#                             Modifying Elements


Sets are mutable but as we can not access elements using index so we can not modify it 



#                          Adding one Element

We can add a new element to set using add( ) method.
Syntax:- 
set_name.add(new_element)
a.add(‘Python’)



#                             Adding Multiple Elements


We can add multiple elements to set using update( ) method. 
The update() method can take tuples, lists, strings or other sets as its argument.
Syntax:- set_name.update(elements)
Ex:-
a.update([101, 102, 103])



#                                   Deleting Element


We can delete element using remove ( ) or discard( ) methods.
Remove( ) method raise an error if element doesn’t exists while discard( ) method remains unchanged.
Syntax:-  set_name.remove(element)
set_name.discard(element)
Ex:-
a.remove(‘GeekyShows’)
a.discard(‘GeekyShows’)



#                                    Copying Elements


Copy ( ) Method is used to copy existing set’s elements into another set.
Syntax:- new_set_name = set_name.copy()
Ex:- new_a = a.copy()



#                                        Clearing All Elements


Clear ( ) Method is used remove all elements to the set
Syntax:- set_name.clear()
Ex:- a.clear()



#                                   intersection() 

intersection() :

The intersection() method returns a set that contains the similarity between two or more sets.

Syntax
set.intersection(set1, set2 ... etc)



#                                         union ( )


The union() method returns a set that contains all items from the original set, and all items from the specified set(s).

You can specify as many sets you want, separated by commas.

It does not have to be a set, it can be any iterable object.

If an item is present in more than one set, the result will contain only one appearance of this item.


Syntax
set.union(set1, set2...)



#                                         difference ( )


The difference() method returns a set that contains the difference between two sets.

Meaning: The returned set contains items that exist only in the first set, and not in both sets.


Syntax
set.difference(set)



#                                            issubset ( )


The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.

Syntax
set.issubset(set)



#                                             issuperset ( )



The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.


Syntax
set.issuperset(set)



