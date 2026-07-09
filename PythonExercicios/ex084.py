from os import system
system('cls')
dados = list()
p_cadastradas = 0
maior_peso = 0
menor_peso = 0
while True:
    dados.append([str(input('Nome: ')), float(input('Kg: '))])
    p_cadastradas += 1
    resp = str(input('Quer Continuar[S/N]: '))
    if resp in 'Nn': 
        break
    #print(dados)

print(f'Numero de Pessoas Cadastradas: {p_cadastradas}')

for dado in dados:
    if dado[1] > maior_peso:
        maior_peso = dado[1]
    
    if menor_peso == 0:
        menor_peso = dado[1]
    elif dado[1] < menor_peso:
        menor_peso = dado[1]

print(f'Maior Peso Registrado: {maior_peso:.2f} Kg de ', end='')
for dado in dados:
    if dado[1] == maior_peso:
        print(dado[0])

print(f'Menor Peso Registrado: {menor_peso:.2f} Kg ', end='') 
for dado in dados:
    if dado[1] == menor_peso:
        print(dado[0])   
