#%%
import pandas as pd
import datetime
#%%
df = pd.read_excel('../data/transactions.xlsx')
df
#%%
(df[['IdCustomer', 'Points']].
 groupby(by = 'IdCustomer').
 sum().
 sort_values(by = 'Points', ascending = False)
)
#%%
# Serie
(df[['IdCustomer','Points']].
 groupby('IdCustomer')['Points'].
 mean().
 sort_values())

# DataFrame
(df[['IdCustomer','Points']].
 groupby('IdCustomer')['Points'].
 mean().
 sort_values().
 reset_index())
#%%
df.groupby('IdCustomer').count()
#%%
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby('IdCustomer').
    agg({'Points': 'sum',
      'UUID': 'count',
      'DtTransaction': ['max', recencia]}).
    rename(columns = {'Points': 'Valor',
                      'UUID': 'Frequencia',
                      'DtTransaction': 'UltimaData'}).
    reset_index())