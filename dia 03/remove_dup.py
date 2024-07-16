#%%
import pandas as pd

#%%
data = {
    'Nome': ['Téo', 'Nah', 'Maria', 'Nah', 'Lara', 'Téo',],
    'Idade': [32, 33, 2, 33, 31, 32],
    'Updated_at': [1, 2, 3, 1, 2, 3]
}

df = pd.DataFrame(data)

#%%
df.drop_duplicates('Nome')

#%%
df = df.sort_values(by = 'Updated_at',
                    ascending = False)
df

#%%
df.drop_duplicates(subset = ['Nome', 'Idade'], keep = 'first')