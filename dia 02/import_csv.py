#%%
import pandas as pd
 #%%

df_customers = pd.read_csv('..\data\customers.csv', sep = ';')
df_customers

#%%
df_customers.shape

#%%
df_customers.info(memory_usage = 'deep')

#%%

df_customers['Points'].describe()

#%%
df_customers.info()

#%%
df_customers.loc[df_customers['Points'] == '59a', 'Points'] = '59'

#%%
df_customers['Points'] = df_customers['Points'].astype(int)

#%%
df_customers['Points'].describe()

#%%
df_customers['Name'][df_customers['Points'].max()]

#%%
df_customers['Points'] > 1000

#%%
df_customers[df_customers['Points'] == df_customers['Points'].max()]

#%%
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name'].loc[436]

#%%
df_customers[(df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)].sort_values(by = 'Points')

#%%
df_customers[['Name', 'Points']]

#%%
df_customers[['Name', 'Points']].sort_values(by = 'Name')

#%%
colunas = df_customers.columns.to_list()
colunas.sort()

df_customers = df_customers[colunas]
df_customers

#%%
df_customers.rename(columns = {'Name': 'Nome', 
                               'Points': 'Pontos',
                               'UUID': 'Id'},
                    inplace = True)

#%%
df_customers
