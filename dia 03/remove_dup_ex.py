#%%
import pandas as pd

df = pd.read_excel('../data/transactions.xlsx')
df
#%%
df_last = df.sort_values(by = 'DtTransaction', ascending = False)
df_last
#%%
df_last = df.drop_duplicates('IdCustomer')
df_last
#%%
df_last['IdCustomer'].nunique()