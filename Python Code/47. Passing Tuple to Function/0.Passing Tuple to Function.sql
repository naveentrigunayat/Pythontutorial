#                                         Passing Tuple to Function


We can pass a tuple to a function while calling function.
def show(t):
	print(t)
	print(type(t))
	for i in t:
		print(i)

tup = (10, 20, 30, 'GeekyShows‘)
show(tup)



