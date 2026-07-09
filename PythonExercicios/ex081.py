numeros = []
resp = 'S' 
while True:
    numero = int(input('Digite Um Numero:'))
    numeros.append(numero)
    while resp != 'S' or resp != 'N':
        resp = str(input('Quer Continuar [S/N] ')).strip()[0].upper()
        if resp == 'S' or resp == 'N':
            break

    if resp == 'N':
            break
print(f'Voce digitou {len(numeros)} numeros no total')
print(f'A Lista ordenada de forma Decrescente fica {sorted(numeros, reverse=True)}')
if numeros.count(5) > 0:
    print('O valor 5 foi encontrado')
else: 
    print('O valor 5 Nao foi encontrado')