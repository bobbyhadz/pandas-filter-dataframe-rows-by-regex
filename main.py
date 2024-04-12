# Filter rows in a Pandas DataFrame using Regex

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Alex', 'Bobby', 'Tony', 'Ethan'],
    'sales': [1, 3, 5, 7, 7],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

regex = r'^Al'

starting_with = df[df['name'].str.contains(regex)]

#     name  sales  salary
# 0  Alice      1   175.1
# 1   Alex      3   180.2
print(starting_with)