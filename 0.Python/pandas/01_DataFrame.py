import pandas as pd

# notes: Series指的是表格中的一列，多个Series组成一个DataFrame


# notes: 使用dict创建DataFrame
data = {
    'apple': [3, 2, 0, 1],
    'orange': [0, 3, 7, 2]
}
purchases = pd.DataFrame(data)
print(purchases, '\n')

# notes: DataFrame的第一列是Index，可以对其进行设置
purchases = pd.DataFrame(data, index=['zhangsan', 'lisi', 'wangwu', 'zhaoliu'])
print(purchases, '\n')

# notes：访问某一行数据
print(purchases.loc['zhangsan'], '\n')