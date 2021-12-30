
'''

Question:

Please write a program which prints all permutations of [1,2,3]


Hints:
Use itertools.permutations() to get permutations of list.

Solution:

'''

"""Solution by: popomaticbubble
"""
from itertools import permutations

def permuation_generator(iterable):
    p = permutations(iterable)
    for i in p:
        print(i)


x = [1,2,3]
permuation_generator(x)
