#%%
import pandas as pd
#%%
df_customer = pd.read_csv('../data/customers.csv', sep = ';')
df_customer
#%%
df_transaction = pd.read_excel('../data/transactions.xlsx')
df_transaction
#%%
df_transactions_product = pd.read_parquet('../data/transactions_cart.parquet')
df_transactions_product
#%%
df_join = (df_transaction.merge(df_customer,
                                how = 'inner',
                                left_on = 'IdCustomer',
                                right_on = 'UUID',
                                suffixes = ['_transacao', "_cliente"])
                         .merge(df_transactions_product,
                                how = 'inner',
                                left_on = 'UUID_transacao',
                                right_on = 'IdTransaction'))
df_join