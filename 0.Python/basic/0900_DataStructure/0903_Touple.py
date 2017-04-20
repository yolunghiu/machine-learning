# 定义Tuple的方式
t = 'zhangsan', 'beijing', 23
print(t)

print(t[0])
# t[0] = 'lisi'     error:tuple不可改变

# tuple中可以包含可改变的对象
t2 = [1,2,3], [4,5,6]
print(t2)
t2[0].reverse()
t2[1].reverse()
print(t2)

# tuple大小
print(len(t2))