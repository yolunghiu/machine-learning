name = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
name2 = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
name3 = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']

# 使用索引的方式删除元素
del name[0]
print(name)

# 类似MATLAB的索引方式，删除从1到2的元素（下标从0开始）
del name2[1:3]
print(name2)

# 清空list
del name3[:]
print(name3)

# 删除变量
del name
