nome = str(input('Informe o nome completo de uma pessoa: '))
nome_repartido = nome.split()
print('Primeiro Nome: {}'.format(nome_repartido[0]))
print('Ultimo Nome: {}'.format(nome_repartido[-1]))