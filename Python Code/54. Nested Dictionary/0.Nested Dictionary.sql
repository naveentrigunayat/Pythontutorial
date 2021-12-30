#                                             Nested Dictionary


A dictionary within another dictionary is called as nested dictionary or nesting of a dictionary.
nested_dict = { 'dict1': {'key_A': 'value_A'}, 
                         'dict2': {'key_B': 'value_B'} } 



#                                  Creating Empty Nested Dict


Syntax:-
nested_dict = { 'dict1': { }, 
                         'dict2': { } } 
Ex:-
a = {1: { },
        2: { } }




#                                Creating Nested Dict


Syntax:-
nested_dict = { 'key_A': 'value_A', 'dict1': {'key_A': 'value_A'} } 
Ex:-
a = {‘course’: ‘Python’, ‘fees’:15000, 1: {‘course’: ‘JavaScript’, ‘fees’: 10000 } }



#                            Accessing Dictionary


a = {‘course’: ‘Python’, ‘fees’:15000, 1: {‘course’: ‘JavaScript’, ‘fees’: 10000 } }

print(a[‘course’])
print(a[‘fees’])

print(a[1][‘course’])
print(a[1][‘fees’])



#                              Modifying Nested Dict


a = {‘course’: ‘Python’, ‘fees’:15000, 1: {‘course’: ‘JavaScript’, ‘fees’: 10000 } }
a[‘course’] = ‘Machine Learning’
a[1][‘fees’] = 200000



#                               Creating Nested Dict



Syntax:-
nested_dict = { 'dict1': {'key_A': 'value_A'}, 
                         'dict2': {'key_B': 'value_B'} } 
Ex:-
a = {1: {‘course’: ‘Python’, ‘fees’:15000},
        2: {‘course’: ‘JavaScript’, ‘fees’: 10000 } }



#                                    Accessing Dictionary


a = {1: {‘course’: ‘Python’, ‘fees’:15000},
        2: {‘course’: ‘JavaScript’, ‘fees’: 10000 } }

print(a[1][‘course’])
print(a[1][‘fees’])

print(a[2][‘course’])
print(a[2][‘fees’])



#                                    Modifying Nested Dict


a = {1: {‘course’: ‘Python’, ‘fees’:15000},
        2: {‘course’: ‘JavaScript’, ‘fees’: 10000 } }
a[1][‘course’] = ‘Machine Learning’
a[2][‘fees’] = 200000
