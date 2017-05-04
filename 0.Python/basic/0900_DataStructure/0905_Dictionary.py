# Dictionary类似于Map，其数据格式
tel = {'jack': 4098, 'sape': 4139}
tel2 = dict(sape=4139, guido=4127, jack=4098) #使用dict()构造方法
print(tel)
print(tel2)

# 添加值
tel['guido'] = 4127
print(tel)

# 按键取值
print(tel['jack'])

# 删除
del tel['sape']
print(tel)

# 获取key
print(list(tel.keys()))

# 判断元素是否存在
print('guido' in tel)