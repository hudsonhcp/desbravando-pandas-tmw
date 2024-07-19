#%%
import pandas as pd
#%%
df = pd.read_csv('../data/dfs_concat.csv', sep = ';')
df
#%%
df = df.set_index(['cod','nome','período'])
#%%
df
#%%
df.stack()
#%%
df_stack = df.stack().reset_index().rename(columns = {'level_3': 'Tipo Homicídio',
                                           0: 'Qntd'})
#%%
df_stack
#%%
df_unstack = (df_stack.
              set_index(['cod','nome','período', 'Tipo Homicídio']).
              unstack().
              reset_index())
df_unstack
#%%
homocidios = df_unstack['Qntd'].columns.to_list()
homocidios
#%%
df_unstack.columns = ['cod', 'nome', 'período'] + homocidios
df_unstack