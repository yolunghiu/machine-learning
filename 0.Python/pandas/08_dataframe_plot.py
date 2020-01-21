import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")

movies_df.plot(kind='scatter', x='Rating', y='Revenue (Millions)', title='Revenue (millions) vs Rating')
plt.show()

movies_df['Rating'].plot(kind='hist', title='Rating')
plt.show()
