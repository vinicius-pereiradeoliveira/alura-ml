from dados import carregar_acessos

# variaveis x e y recebem os valores da funcao
# carregar_acessos() do arquivo dados.py 
x, y = carregar_acessos()

# 90 elemntos de treino
treino_dados = x[:90] # primeiras 90 linhas do array x
treino_marcacoes = y[:90] # primeiras 90 linhas do array y

# 9 elementos de teste
teste_dados = x[-9:] # ultimas 9 linhas
teste_marcacoes = y[-9:] # ultimas 9 linhas, serve de parametro para comparacao

# importa da lib sklearn a funcao MultinomialNB para treinar modelos  
from sklearn.naive_bayes import MultinomialNB

# variavel modelo recebe a funcao de treinamento
modelo = MultinomialNB()

# variavel de treinamento se ajusta (fit) aos dados de treinamento dados
# e treinamento marcacoes
modelo.fit(treino_dados,treino_marcacoes)

# faz previsao (predict) com os dados de teste, ultimas 9 linhas
resultado = modelo.predict(teste_dados)

# aqui calcula o resultado do teste de dados o teste de marcacoes parametro a ser alcancado
diferencas = resultado - teste_marcacoes

# joga em acertos a iteracao em todas as diferencas, nelas verifica
# se d == 0 se for eh acerto
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

# calcula taxa de acerto
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print (taxa_de_acerto)
print (total_de_elementos)
resultado

