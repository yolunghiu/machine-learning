import numpy as np

a = np.array([[1,1,1], [2,2,2], [3,3,3],[4,4,4],[5,5,5]])
print('a: ')
print(a)

segments = 5;

b = []
b = np.array_split(a, segments)
print('b: ')
print(b)

c = np.concatenate((b[0],b[1]))
print('c: ')
print(c)

# 去掉第二段
d = np.zeros((1,3))

for i in range(segments):
	if i != 1:
		d = np.concatenate((d,b[i]))

d = d[1:,:]
print('d: ')
print(d)


