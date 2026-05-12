from os import system
system('clear')
maior_idade = 0
quant_homens = 0
quant_mulheres = 0 
while True:
	idade = int(input('Informe sua idade: '))
	while True:
		sexo = str(input('Informe seu sexo [M/F]: ')).strip()[0].upper()
		if sexo == 'M' or sexo == 'F':
			break
	if idade >= 18:
		maior_idade = maior_idade + 1
	if sexo == 'M':
		quant_homens = quant_homens + 1
	if idade < 20 and sexo == 'F':
		quant_mulheres += 1
	resp = str(input('Deseja Continuar[S/N]')).strip()[0].upper()
	if resp == 'N':
		break
print(f'Pessoas com 18 anos ou mais: {maior_idade} \nHomens Cadastrados: {quant_homens}')
print(f'Mulheres Com menos de 20 anos: {quant_mulheres}')
