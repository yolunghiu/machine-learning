import numpy as np

a = np.array([[1,0,0,1],[0,0,0,1]])
# oneIndex = np.where(a>0)
[x,y] = np.where(a>0)
print('a:\n',a)
print('x:\n',x)
print('y:\n',y)
# print(oneIndex)