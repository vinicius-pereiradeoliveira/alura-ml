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