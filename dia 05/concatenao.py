#%%
import pandas as pd
#%%
df_01 = pd.read_csv('../data/ipea/homicidios.csv', sep = ';')
df_01 = df_01.rename(columns = {'valor': 'homicidios'})
df_01
#%%
df_02 = pd.read_csv('../data/ipea/homicidios-por-armas-de-fogo.csv', sep = ';')
df_02 = df_02.rename(columns = {'valor': 'homicidios-por-armas-de-fogo'})
df_02
#%%
df_01 = df_01.set_index(['cod', 'nome', 'período'])
df_02 = df_02.set_index(['cod', 'nome', 'período'])
#%%
df_01
#%%
df_02
#%%
pd.concat([df_01, df_02], axis = 1)
#%%
pd.concat([df_01, df_02], axis = 1).reset_index()
#%%
import os

def import_etl(path: str):
    name = path.split('/')[-1].split('.')[0]

    df = (pd.read_csv(path, sep = ';').
          rename(columns = {'valor': name}).
          set_index(['cod', 'nome', 'período']))
    
    return df

path = '../data/ipea/'
files = os.listdir(path)
#%%
# dfs = [import_etl(path + i) for i in files]

dfs = []
for i in files:
    dfs.append(import_etl(path + i))

#%%
dfs_concats = pd.concat(dfs, axis = 1).reset_index()
dfs_concats.to_csv('../data/dfs_concat.csv', sep = ';', index = False)
