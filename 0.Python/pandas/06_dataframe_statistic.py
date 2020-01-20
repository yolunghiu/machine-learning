import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
flag = False

# notes: 获取统计数据
flag = not flag
if flag:
    print(movies_df.describe())  # 所有列的统计数据信息
    print('-' * 40)

    print(movies_df['Genre'].describe())  # 一列的统计数据
    print('-' * 40)

    print(movies_df['Genre'].value_counts().head(10))  # 出现频率最高的前十条记录
    print('-' * 40)

    print(movies_df.corr())  # 协方差矩阵
    print('-' * 40)
