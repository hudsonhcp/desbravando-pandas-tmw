#%%
import pandas as pd

#%%
data = {
    'nome': ['teo', 'nag', 'lara', 'maria'],
    'sobrenome': ['calvo', 'ataide', 'calvo', 'calvo'],
    'idade': [31, 32, 31, 2]
}

#%%
data['idade'][0]

#%%
df = pd.DataFrame(data)

df

#%%
df['idade'].iloc[0]

#%%
df['sobrenome'].iloc[0]

#%%
df.iloc[0]

#%%
df.index

#%%
df.columns

#%%
df.dtypes

#%%
df['peso'] = [80, 53, 65, 14]

df.describe()