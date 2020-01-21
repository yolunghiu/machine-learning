import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
flag = False

# notes: 访问DataFrame中的Series(列)直接通过[]访问
# flag = not flag
if flag:
    movies_df.columns = [col.lower() for col in movies_df]
    genre_col = movies_df['genre']
    print(type(genre_col))  # pandas.core.series.Series

    # notes: 将DataFrame中某些Series组合成新的DataFrame
    genre_col = movies_df[['genre']]
    print(type(genre_col))  # pandas.core.frame.DataFrame
    subset = movies_df[['genre', 'rating']]
    print(subset.head())

# notes: 访问DataFrame中的某些行，使用.loc, .iloc，{.loc["name"]通过第一列关键字检索}， {.iloc[index]通过行号检索}
# flag = not flag
if flag:
    # prom = movies_df.loc["Prometheus"]
    prom = movies_df.loc[1]
    print(prom)
    print('-' * 70)
    prom = movies_df.iloc[1]
    print(prom)

# notes: slice访问数组的方式同样可以使用
# flag = not flag
if flag:
    movie_subset = movies_df.loc['Prometheus':'Sing']
    print(movie_subset, '\n')
    movie_subset = movies_df.iloc[1:4]
    print(movie_subset, '\n')

# notes: 条件过滤
flag = not flag
if flag:
    condition = (movies_df['Director'] == "Ridley Scott")
    print(condition.head())
    print('type: {}'.format(type(condition)))
    print('shape: {}'.format(condition.shape))

    filtered_movie = movies_df[condition]
    print(filtered_movie.head())

    filtered_by_director = movies_df[movies_df['Director'].isin(['Christopher Nolan', 'Ridley Scott'])]
    print(filtered_by_director.head())
