#%%
import pandas as pd

#%%

df = pd.read_excel('../data/transactions.xlsx')
df

#%%
df.shape

#%%
df.head()

#%%
df.tail()

#%%
colunas = df.columns.to_list()

colunas_ordenadas = [colunas[0], colunas[3], colunas[1], colunas[2]]
colunas_ordenadas

df.columns = colunas_ordenadas
df

#%%
df.info(memory_usage = 'deep')