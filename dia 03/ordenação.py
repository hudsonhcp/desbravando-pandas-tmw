#%%
import pandas as pd

#%%

df = pd.read_csv('../data/customers.csv', sep = ';')
df

#%%
# Ordenação por pontos de forma descrescente e, em caso de empate, ordenação por Nome em forma crescente
df.sort_values(by = ['Points', 'Name'], ascending = [False, True])

#%%
# Ordenação por pontos de forma descrescente e, em caso de empate, ordenação por Nome em forma crescente, alterando o dataframe
# Alteração também das colunas 'Name' e 'Points'
df = (df.sort_values(by = ['Points', 'Name'], 
                     ascending = [False, True])
        .rename(columns = {'Name': 'Nome',
                           'Points': 'Pontos'}))

df