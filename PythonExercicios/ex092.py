import datetime
from os import system
 
system('cls')
date = datetime.date.today()
year = date.strftime('%Y')

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = int(year) - ano_nasc
pessoa['ctps'] = int(input('Carteira de Trabalho(0 nao tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Qual o Salario R$: '))
    pessoa['Aposentadoria'] = pessoa['contratacao'] + 35 - ano_nasc
print('-='*30)
for k, v in pessoa.items():
    print(f'{k} tem valor {v}')