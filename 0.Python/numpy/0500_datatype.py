import numpy as np

# 创建数组时，numpy可以自动选择数据类型
x = np.array([1,2])
print(x.dtype)

x = np.array([1.0,2.0])
print(x.dtype)

x = np.array([1,2], dtype=np.int64)
print(x.dtype)

