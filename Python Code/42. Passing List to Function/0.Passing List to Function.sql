#                                          Passing List to Function


We can pass a list to a function while calling function.
def show(l):
	print(l)
	print(type(l))
	for i in l:
		print(i)

lst = [10, 20, 30, 'GeekyShows']
show(lst)


