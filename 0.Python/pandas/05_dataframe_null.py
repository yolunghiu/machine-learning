import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
flag = False

# notes: work with missing values
flag = not flag
if flag:
    impute = True
    if not impute:
        nulls = movies_df.isnull().sum()
        print(nulls)
        movies_df.dropna(inplace=True)  # 直接删除含有null值的row
        print(movies_df.shape)
    else:
        revenue = movies_df['Revenue (Millions)']
        print(revenue.head(), '\n')
        mean = revenue.mean()
        print('mean: {}\n'.format(mean))
        print(movies_df.isnull().sum(), '\n')
        revenue.fillna(mean, inplace=True)  # 使用均值填充null值
        print(movies_df.isnull().sum(), '\n')
