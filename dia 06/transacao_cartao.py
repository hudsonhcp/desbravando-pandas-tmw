#%%
import pandas as pd
#%%
df = pd.read_excel('../data/transacao_cartao.xlsx')
df
#%%
df['dtTransaction'] = pd.to_datetime(df['dtTransaction'], format = "%d/%m/%Y")
#%%
# df['ValorParcela'] = df['Valor'] / df['Parcelas']
df
#%%
df
#%%
df['ValorParcela'] = df.apply(lambda row: [row['Valor'] / row['Parcelas'] for _ in range(row['Parcelas'])], axis = 1)
df
#%%
df_fatura = df.explode('ValorParcela')
#%%
df_fatura
#%%
df_fatura['Months_add'] = df_fatura.groupby(by = 'IdTransaction')['dtTransaction'].rank('first').astype(int)
#%%
df_fatura
#%%
import numpy as np
def add_months(row):
    new_date = row['dtTransaction'] + np.timedelta64(row['Months_add'], "M")
    dt_str = f'{new_date.year}-{new_date.month:02}'
    return dt_str

df['dtFatura'] = df_fatura.apply(add_months, axis = 1)
#%%
df_fatura_mes = df_fatura.groupby(['idCliente', 'dtFatura'])['ValorParcela'].sum()
df_fatura_mes = df_fatura_mes.reset_index()
#%%
df_fatura_mes = df_fatura_mes.pivot_table(columns = 'dtFatura',
                                          index = 'idCliente',
                                          values = 'ValorParcela')

df_fatura_mes = df_fatura_mes.fillna(0)
df_fatura_mes
#%%
df_fatura_mes.to_excel('fatura_detalhada.xlsx')