def multiReturn():
	a = 1
	b = 2
	c = 3

	return {a, b, c}

a, b, c = multiReturn()
print('a:', a)
print('b:', b)
print('c:', c)