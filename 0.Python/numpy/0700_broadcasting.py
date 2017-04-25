import numpy as np

# 通常情况下，在numpy环境下进行的数组计算都要满足维数要求
a = np.array([1,2,3])
b = np.array([2,3,4])

print(a * b)    # [ 2  6 12]

print('\n-------------------------\n')

# broadcasting降低了这个要求，下面是一个最简单的例子
a = np.array([1,2,3])
b = 2
print(a * b)

# 上面两个例子完成的是一样的功能，但是第二个例子更高效