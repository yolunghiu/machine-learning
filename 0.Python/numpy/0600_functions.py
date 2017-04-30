import numpy as np

x = np.array([[1,2],[3,4]])

# 计算所有元素的和
print(np.sum(x))

# 计算每列的和
print(np.sum(x, axis=0))

# 计算每行的和
print(np.sum(x, axis=1))

# 转置
print(x.T)

# 找到数组中某元素的索引
y = np.array([1,2,3])
print(np.where(y==3)[0])