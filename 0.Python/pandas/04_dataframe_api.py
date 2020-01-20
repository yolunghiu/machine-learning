import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
flag = False

# notes: 读入数据之后，首先打印一些缩略信息
# flag = not flag
if flag:
    head = movies_df.head()
    print(head, '\n')
    print(movies_df.head(10))  # 输出前10条
    print(movies_df.tail())
    print(movies_df.tail(10))

# notes: 数据相关信息
# flag = not flag
if flag:
    info = movies_df.info()
    print('info: {}\n'.format(info))

# notes: 表格尺寸
# flag = not flag
if flag:
    shape = movies_df.shape
    print('shape: {}\n'.format(shape))

# notes: 去重
# flag = not flag
if flag:
    tmp_df = movies_df.append(movies_df)
    print(tmp_df.shape)
    tmp_df = tmp_df.drop_duplicates()
    tmp_df.drop_duplicates(inplace=True)  # in place 操作
    print(tmp_df.shape)
    tmp_df = movies_df.append(movies_df)
    tmp_df.drop_duplicates(inplace=True, keep=False)  # keep: first|last|False
    print(tmp_df.shape, '\n')

# notes: columns cleanup, rename
# flag = not flag
if flag:
    print(movies_df.columns)
    movies_df.rename(columns={
        'Runtime (Minutes)': 'Runtime',
        'Revenue (Millions)': 'Revenue_millions'
    }, inplace=True)
    print(movies_df.columns)

    movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime',
                         'rating', 'votes', 'revenue_millions', 'metascore']
    print(movies_df.columns)

    movies_df.columns = [col.lower() for col in movies_df]
    print(movies_df.columns)