soma = 0
contador = 0
while True:
	numero = int(input('Informe um valor(999 para parar.)'))
	if numero == 999:
		break
	soma = soma + numero
	contador += 1
print(f'A Soma dos {contador} valores e igual {soma}')