from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

maior = 0
menor = 0
print('Os Valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print()

for contador in numeros:
    #maior = contador
    if maior == 0:
        maior = contador
    elif contador > maior:
        maior = contador
    if menor == 0:
        menor = contador
    if contador < menor:
        menor = contador
print(f'O maior valor e: {maior}') 
print(f'O menor valor e: {menor}') 