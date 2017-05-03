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
print(np.sum(a, axis = 0))  # 行向量的和
print(np.sum(a, axis = 1))  # 列向量的和

# keepdims参数起到如下作用：
# 	如下的求和函数，设置axis=1后，结果是一个一维的数组,这个数组是所有列的和
# 	如果keepdims = True,则结果依旧保留为一个列向量
# 	如果keepdims = False,则结果就是一个一维数组（默认当成行向量）
b = np.sum(a, axis = 1, keepdims = True)
c = np.sum(a, axis = 1, keepdims = False)

print(b)
print(c)

print(np.shape(b))
print(np.shape(c))
