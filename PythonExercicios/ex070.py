from os import system
system('clear')
preco_barato = 0
produto_barato = ''
total_compra = 0
produtos_mil = 0
while True:
	produto = str(input('Nome do Produto: '))
	preco = float(input('Preço: R$ '))
	total_compra += preco
	if preco_barato == 0:
		preco_barato = preco
	elif preco_barato > preco:
		preco_barato = preco
		produto_barato = produto
	if preco > 1000:
		produtos_mil = produtos_mil + 1 
	resposta = str(input('Quer Continuar ? [S/N]')).strip()[0].upper()
	if resposta == 'N':
		break
	elif resposta != 'S':
		print('Resposta Invalida')
		while resposta != 'S':
			resposta = str(input('Quer Continuar ? [S/N]')).strip()[0].upper()

print(f'O Total da compra foi de R$: {total_compra:.2f}')
print(f'O Produto mais barato foi a {produto_barato} custou R$ {preco_barato:.2f}')
print(f'Total de produtos acima de R$ 1000 foi de {produtos_mil}')