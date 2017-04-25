import numpy as np

a = np.array([1,2,3])
print(a.shape)
print(type(a))
print(a[0], a[1], a[2])

a[0] = 5
print(a)

print('\n----------------------\n')

b = np.array([[1,1,1], [2,2,2]])    # 两行三列
print(b.shape)
print(b[0,0])
print(b)

print('\n----------------------\n')

a = np.array([0, 10, 20, 30])
print(np.shape(a))  # (4,)

b = np.array([1, 2, 3])

# 把a转换成一个列向量
a = a[:, np.newaxis]
print(np.shape(a))  # (4,1)

print(a + b)
