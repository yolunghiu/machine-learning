import numpy as np

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# 2 3
# 6 7
b = a[:2,1:3]

print(a[0,1])   #2

# 对b的修改会反映到a上
b[0,0] = 77;

print(a[0,1])   #77

# ---------------------------

# 把indexOfArr数组作为arr数组的索引，来访问arr数组
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

indexOfArr = np.array([0,1,2])
print(arr[np.arange(3), indexOfArr])
