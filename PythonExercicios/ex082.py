from os import system
system('cls')
numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite Um Numero: ')))
    resp = str(input('Quer Continuar [S/N]: ')).strip()[0].upper()
    if numeros[-1] % 2 == 0:
        pares.append(numeros[-1])
    else:
        impares.append(numeros[-1])
    while resp != 'S' and resp != 'N':
        print('Resposta Invalida')
        resp = str(input('Quer Continuar [S/N]: ')).strip()[0].upper()
    if resp == 'S':
        continue
    elif resp == 'N':
        break

print(f'Lista Original: {numeros}...')
print(f'Lista de  Numeros Pares: {pares}...')
print(f'lista de Numeros Impares: {impares}...')