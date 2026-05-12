while True:
	numero = int(input('Digite um numero: '))
	resp = str(input('Quer Continuar ? [S/N]')).strip().upper()[0]
	while resp != 'S':
		resp = str(input('Quer Continuar ? [S/N]')).strip().upper()[0]
		if resp == 'N':
			break
	if resp == 'N':
		break