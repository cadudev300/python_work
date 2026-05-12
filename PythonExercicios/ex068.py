from random import randint
from os import system
system('clear')
tot_vitoria = 0
resultado = ''
computador = 0
while True:
	print('Vamos Jogar Par ou Impar')
	numero = int(input('Digite um valor: '))
	computador = randint(0, 100)
	opcao = str(input('Par Ou Impar [P/I]')).strip()[0].upper()
	print(f'Voce Jogou {numero} e o computador {computador}', end=' ')
	print(f'Total = {numero + computador}', end=' ')
	while True:
		if opcao == 'P' or opcao == 'I':
			break
		else:
			opcao = str(input('Par Ou Impar [P/I]')).strip()[0].upper()
	if opcao == 'P':
		valor = numero + computador
		if valor%2 == 0:
			resultado = 'Jogador Ganhou !!!'
			tot_vitoria = tot_vitoria + 1
			print('Voce Ganhou Vamos Jogar Novamente')
		else:
			resultado = 'Computador Ganhou !!!'
	elif opcao == 'I':
		valor = numero + computador
		if valor%2 != 0:
			resultado = 'Jogador Ganhou !!!'
			tot_vitoria += 1
			print('Voce Ganhou Vamos Jogar Novamente')
		else:
			resultado = 'Computador Ganhou !!!'
	if resultado == 'Computador Ganhou !!!':
		break
print(f'Resultado: {resultado}', end=' ')
print(f'Numero de Vitorias {tot_vitoria}')