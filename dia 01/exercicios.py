#%%
import pandas as pd

#%%

"""Converta a seguinte lista de dados para uma Series Pandas e obtenha:
Média
Desvio Padrão
Máximo Valor

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
"""

dados = pd.Series([10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21])

print('Média: ', round(dados.mean(), 2))
print('Desvio padrão: ', round(dados.std(), 2))
print('Máximo Valor: ', dados.max())

#%%

"""Converta o seguinte dicionário para DataFrame e obtenha:
Sumário de cada coluna
Média da coluna idade
Último nome da coluna nome

dados = {“nome”:[“Téo”, “Nah”, “Napoleão”], “idade”: [31, 32, 14]}"""

df = pd.DataFrame({'nome': ['Téo', 'Nah', 'Napoleão'],
                  'idade': [31, 32, 14]})

print('Sumário de cada coluna')
print(df.describe())
print('Média da coluna idade: ', round(df.describe()['idade']['mean'], 2))
print('Último nome da coluna nome: ', df['nome'].iloc[-1])