import csv

def carregar_acessos():

	x = []
	y = []

	arquivo = open('arquivo.csv', 'rb')
	leitor = csv.reader(arquivo)

	leitor.next()

	for home, como_funciona, contato, comprou in leitor:

	    x.append([int(home), int(como_funciona), int (contato)])
	    y.append(int(comprou))

	return x, y

def carregar_buscas():

	x = []
	y = []

	arquivo = open('busca.csv', 'rb')
	leitor = csv.reader(arquivo)

	leitor.next()

	for home, busca, logado, comprou in leitor:

	    x.append([int(home), busca, int (logado)])
	    y.append(int(comprou))

	return x, y    