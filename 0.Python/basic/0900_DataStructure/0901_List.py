# List中可以包含重复的元素，可以按索引访问
a = [66.25, 333, 333, 1, 1234.5]

print('a的类型：' + type(a).__name__)

print('333出现的次数：' + str(a.count(333)))

print('a的长度：', len(a))
print('遍历a：')
for i in range(len(a)):
	print(a[i])
print('遍历a结束')

# 插入、添加
a.insert(2, -1)
a.append(333)

print(a)

# 索引
print(a.index(333))

# 删除
a.remove(333)

# 取反
a.reverse()

# [0,1,2,3,...]
b = list(range(10))

