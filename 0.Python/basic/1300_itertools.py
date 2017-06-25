import itertools

# (, stop)
result = list(itertools.islice("Hello", 3))
print(result)


# (, start, stop)
def sayHi():
	return "Hi"

result2 = list(itertools.islice(sayHi(), 3))
print(result2)