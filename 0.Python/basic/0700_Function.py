# 定义一个函数
def test():
    print('----哈哈----')


# 调用函数
test()


# 带参数的函数
def sayHi(name, student=False):
    if student:
        print('Hi student ' + name)
    else:
        print('Hi ' + name)

sayHi('zhangsan')
sayHi('lisi', student=True)