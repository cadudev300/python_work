from os import system
system('cls')
matriz = [[],[],[]]
soma_par = 0
tot_3 = 0
maior_valor = 0

for linha in range(0, 3):
    #matriz.append([])
    for coluna in range(0, 3):
        valor = int(input(f'Digite Um Valor em [{linha} {coluna}] '))
        matriz[linha].append(valor)
        if valor % 2 == 0:
            soma_par = soma_par + valor
            
for linha in range(0, 3): 
    tot_3 = tot_3 + matriz[linha][2]
    if matriz[1][linha] > maior_valor:
        maior_valor = matriz[1][linha]

for linha in range (0, len(matriz)):
    for coluna in range (0, len(matriz)):
        print(f' [ {matriz[linha][coluna] } ] ', end='')
    print()
print(f'A Soma dos Valores Pares {soma_par}')
print(f'A soma dos valores da 3° coluna: {tot_3} ')
print(f'Maior Valor da 2° Linha: {maior_valor}')
