import pandas as pd

df = pd.read_json('purchases.json')
print(df)

df.to_json('new_purchases.json')