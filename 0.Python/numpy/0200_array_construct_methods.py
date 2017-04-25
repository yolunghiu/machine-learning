import numpy as np

# 定义所有元素都是0的矩阵
zero = np.zeros((2,2))
print(zero)

# 定义所有元素都是1的矩阵
one = np.ones((2,2))
print(one)

# 定义所有元素都是7的矩阵
full = np.full((2,2), 7)
print(full)

# 定义二维单位矩阵
eye = np.eye(2)
print(eye)

# 定义随机数矩阵
random = np.random.random((2,2))
print(random)