#%%
import pandas as pd

#%%
idades = [18, 21, 9, 42]
idades

#%%
media = sum(idades)/len(idades)
media

#%%
total = 0

for i in idades:
    total += (media - i) ** 2

variancia = total / (len(idades) - 1)

variancia

#%%

series_idades = pd.Series(idades, name = "idades")

print(series_idades.mean())
print(series_idades.var())
print(series_idades.median())

#%%
series_idades

#%%
round(series_idades.describe(), 2)

#%%
series_idades.shape

#%%
series_idades.index = ['a', 'b', 'c', 'd']
series_idades

#%%
series_idades['b':'d']

#%%
series_idades[1]

#%%
series_idades.iloc[3]
