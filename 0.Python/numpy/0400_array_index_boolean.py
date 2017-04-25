import numpy as np

# boolean index 可以用于给定一些条件限制的查询
a = np.array([[1,2],[3,4],[5,6]])

boolean_index = (a > 2)

print(boolean_index)

print(a[boolean_index])
print(a[a > 2])