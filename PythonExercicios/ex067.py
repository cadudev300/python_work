cont = 0
while True:
	numero = int(input('Digite um numero para ver a tabuada: '))
	if numero < 0:
		break
	while cont < 11:
		print(f'{numero} x {cont} = {numero * cont}')
		cont = cont + 1
	cont = 0
print('Fim do Programa ...')