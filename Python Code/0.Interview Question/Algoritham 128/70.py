'''

Question:


Please write assert statements to verify that every number in the list [2,4,6,8] is even.



Hints:
Use "assert expression" to make assertion.


Solution:

'''

data = [2,4,6,8]
for i in data:
    assert i%2 == 0, "{} is not an even number".format(i)

