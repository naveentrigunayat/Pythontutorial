
'''
Question:
Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.

Solution

'''

class American(object):
    @staticmethod
    def printNationality():
        print("I am American")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()