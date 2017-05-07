import numpy as np

a = np.arange(6).reshape(2,3)
print('\na:')
print(a)

print('\n遍历a：默认是行序优先（order=\'C\'）')
for x in np.nditer(a):
	print(x)

print('\n遍历a.T的顺序和上面是一样的，因为在内存中存储的顺序一样')
for x in np.nditer(a.T):
	print(x)

print('\n遍历a.T.copy,是新创建的数组')
for x in np.nditer(a.T.copy(order='C')):
	print(x)

b = np.array([[1,1,1],[2,2,2]])
print('\nb:')
print(b)

# 列序优先遍历(Fortran order)
print('\n列序优先遍历')
for y in np.nditer(b,order='F'):
	print(y)

# 默认情况下，nditer将视待迭代遍历的数组为只读对象（read-only
# 为了在遍历数组的同时，实现对数组元素值得修改，必须指定read-write或者write-only的模式
c = np.array([[0,1,2],[3,4,5]])
print('\nc:')
print(c)

for x in np.nditer(c,op_flags=['readwrite']):
	x[...] = 2*x
print('\n修改后的c：')
print(c)

# 一次取一行
print('\n多维数组的遍历')
d = np.array([[1,1,1],[2,2,2]])
iterator = np.nditer(d, flags=['multi_index'], op_flags=['readwrite'])
while not iterator.finished:
	index = iterator.multi_index
	print(index)
	print(d[index])
	iterator.iternext()
