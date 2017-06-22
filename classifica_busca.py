# usa panda para trabalhar e ler arquivo csv
import pandas as pd
import numpy as np
from collections import Counter

df = pd.read_csv('busca2.csv') # df = dataframe que recebe os dados lidos no csv pelo panda

x_df = df[['home','busca','logado']] # na var x_df coloca as 3 primeiras colunas
y_df = df[['comprou']] # na var y_df coloca a ultima coluna

xdummies_df = pd.get_dummies(x_df).astype(int)
ydummies_df = y_df

x = xdummies_df.values # .values transforma os valores de dummies em array
y = ydummies_df.values

# encerrada leitura e organizacao de dados do algoritmo
# ===========================================================================
# inicio de construcao das variaveis de treino e teste dos dados do algoritmo

porcentagem_de_treino = 0.9
'''
tamanho_de_treino = int(porcentagem_de_treino * len(y)) # pega 90 por cento de y
tamanho_de_teste = len(y) - tamanho_de_treino # pega tamanho de y (len) e subtrai o tamanho de treino, restante eh teste

# treina com 90 por cento tamanho_de_treino
treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]
'''

# modelo acima comentado com 1 e 0 e abaixo modelo usando strings sim e nao do arquivo busca2.csv
tamanho_de_treino = int(porcentagem_de_treino * len(y))
tamanho_de_teste = len(y) - tamanho_de_treino

treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]

# testa com restante  tamanho_de_teste
teste_dados = x[-tamanho_de_teste:]
teste_marcacoes = y[-tamanho_de_teste:]

# Agora vamos treinar o modelo de fato com sklearn

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes.ravel())

# treinou, agora vamos fazer a previsao e ver o resultado do treino na var diferencas
resultado = modelo.predict(teste_dados)
diferencas = resultado == teste_marcacoes

'''
acertos = [d for d in diferencas if np.all(d) == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
'''

total_de_acertos = sum(diferencas)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print("Taxa acerto algoritmo:")
print(taxa_de_acerto)
print(total_de_elementos)

acerto_base = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(teste_marcacoes)
print("Taxa acerto base:")
print(taxa_de_acerto_base)