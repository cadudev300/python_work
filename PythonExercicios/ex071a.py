from os import system
system('clear')
valor = int(input('Informe o valor do saque R$ '))
total = valor
cedula = 50
tot_cedulas = 0
while True:
	if total > cedula:
		total = total - cedula
		tot_cedulas = tot_cedulas + 1
	else:
		if tot_cedulas > 0:
			print(f'Total de {tot_cedulas} cedulas de R${cedula} ')
		elif cedula == 50:
			cedula = 20
		elif cedula == 20:
			cedula = 10
		elif cedula == 10:
			cedula = 1
		elif cedula == 1:
			tot_cedulas = 0
		elif tot_cedulas == 0:
			break
print('Acabou')