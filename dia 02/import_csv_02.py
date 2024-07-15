#%%
import pandas as pd

#%%
df = pd.read_csv('..\data\products.csv', 
                 sep = ';',
                 names = ['Id', 'Name', 'Description'])
df

# df.rename(columns = {'0': 'Id', '1': 'Name', '2': 'Description'})

#%%

df.rename(columns = {'Name': 'Nome',
                     'Description': 'Descricao'},
          inplace = True)
df