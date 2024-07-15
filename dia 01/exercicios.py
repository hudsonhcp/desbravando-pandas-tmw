#%%
import pandas as pd

#%%

"""
Converta a seguinte lista de dados para uma Series Pandas e obtenha:
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

"""
Converta o seguinte dicionário para DataFrame e obtenha:
Sumário de cada coluna
Média da coluna idade
Último nome da coluna nome

dados = {“nome”:[“Téo”, “Nah”, “Napoleão”], “idade”: [31, 32, 14]}
"""

df = pd.DataFrame({'nome': ['Téo', 'Nah', 'Napoleão'],
                  'idade': [31, 32, 14]})

print('Sumário de cada coluna')
print(df.describe())
print('Média da coluna idade: ', round(df.describe()['idade']['mean'], 2))
print('Último nome da coluna nome: ', df['nome'].iloc[-1])

#%%
"""
Carregue os dados do arquivo data/ipea/homicidios.csv de forma correta e informe:
Quantidade de linhas
Quantidade de colunas
Nome da primeira coluna
Nome da última coluna
"""

df = pd.read_csv('../data/ipea/homicidios.csv', sep = ';')
df

print(f'Quantidade de linhas: ', df.shape[0])
print(f'Quantidade de colunas: ', df.shape[1])
print(f'Nome da primeira coluna: ', df.columns[0])
print(f'Nome da última coluna: ', df.columns[-1])

#%%
"""
Carregue os dados do arquivo data/ipea/homicidios-mulheres-negras.csv de forma correta e informe:
Quais colunas são do tipo numérico?
Quantas colunas são do tipo ‘object’?
Qual o tamanho destes dados em memória?
"""

df = pd.read_csv('../data/ipea/homicidios-mulheres-negras.csv', sep = ';')

print('Quais colunas são do tipo numérico: ', df.select_dtypes(include = 'int64').columns.to_list())
print('Quantas colunas são do tipo ‘object’: ', df.select_dtypes(include = 'object').columns.to_list())
print('Qual o tamanho destes dados em memória: ', round(df.memory_usage(deep = True).sum()/1024, 1), 'KB')