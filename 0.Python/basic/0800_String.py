s1 = 'hello'
s2 = "world"

# 输出
print(s1)
print(s2)
print("s1 is: %s" %s1)
print("s1 is: " + s1)

# 索引
print('the first word in s2 is: ' + s2[0])
print('the top three words in s2: ', s2[0:3]) # 取出下标为0到2的字符
print(s2[2:]) # 取出下标从2开始，直到最后的字符
print(s2[0:-1]) # 取出下标从0开始，直到最后第二个字符