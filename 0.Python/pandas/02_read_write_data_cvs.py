import pandas as pd

# notes: 直接读取
df = pd.read_csv('purchases.csv')
print(df)

# notes：读取时指定index_col
df = pd.read_csv('purchases.csv', index_col=0)
print(df)

# notes: 写入cvs
df.to_csv('new_purchases.csv')