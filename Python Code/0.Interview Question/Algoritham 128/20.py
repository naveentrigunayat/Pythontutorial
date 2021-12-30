'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield



#Solution:
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in putNumbers(100):
    print(i)


'''





class iterator(object):
	"""docstring for iterator"""
	def __init__(self, n):
		super(iterator, self).__init__()
		self.n = n
		
	def divBySeven(self):
		for i in range(0, self.n):
			if i % 7 == 0:
				yield i

for num in iterator(100).divBySeven():
	print(num)