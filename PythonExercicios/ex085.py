from os import system
system('cls')
numeros = [[],[]]
for i in range(0, 7):
    numero = int(input(f'Digite o {i}° valor: '))
    if numero%2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print(f'Valores Pares em ordem Crescente: {sorted(numeros[0])}')
print(f'Valores Impares em ordem Crescente: {sorted(numeros[1])}')