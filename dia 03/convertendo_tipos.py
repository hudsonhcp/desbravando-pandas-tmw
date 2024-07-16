#%%
import pandas as pd

df = pd.read_csv('../data/customers.csv', sep = ';')
df
#%%
df.dtypes
#%%
df['Points'] = df['Points'].astype(str)
#%%
df['Points'] = 'R$ ' + df['Points']
df