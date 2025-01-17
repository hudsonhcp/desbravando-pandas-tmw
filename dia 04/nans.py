#%%
import pandas as pd
import numpy as np
#%%
data = {
    'nome': ['Téo', 'Nah', 'Lah', 'Mah', 'Jo'],
    'idade': [31, 32, 34, 12, np.nan],
    'renda': [np.nan, 3245, 357, 12432, np.nan]
}

df = pd.DataFrame(data)
df
#%%
df['idade'].isna().sum()
#%%
df.isna().mean()

df.isna().sum() / (df.notna().sum() + df.isna().sum())
#%%
df.notna().mean()
#%%
df.fillna({
    'idade': df['idade'].mean(),
    'renda': df['renda'].mean()
})
#%%
# Remove todas as linhas totalmente NaN
df.dropna(how  = 'all')

df.dropna(subset = ['idade', 'renda'], how = 'all')
#%%
df.dropna(axis = 1)