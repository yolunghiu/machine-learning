import numpy as np

a = np.array([1,2,3])
print(a.shape)
print(type(a))
print(a[0], a[1], a[2])

a[0] = 5
print(a)

print('----------------------')

b = np.array([[1,1,1], [2,2,2]])    # 两行三列
print(b.shape)
print(b[0,0])
print(b)