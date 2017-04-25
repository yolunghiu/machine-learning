import numpy as np

# 获得数组的维度，类似MATLAB中的size函数
a = np.array([[1,1,1], [2,2,2]])
print(a.shape)
print(a.shape[0])
print(a.shape[1])

print('-------------')

# Python中的for in
dementionX = a.shape[0]
print(dementionX)

for i in range(dementionX):
    print(i)

print('-------------')

# Python中的sum函数对数组的操作
a = np.array([[1,2],[3,4]])
print(np.sum(a))            # 所有元素的和
print(np.sum(a, axis = 0))  # 所有列的和
print(np.sum(a, axis = 1))  # 所有行的和