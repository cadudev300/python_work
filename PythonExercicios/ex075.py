from os import system
system('cls')
posicao_3 = 0
numeros = (int(input('Digite Um Numero: ')),
            int(input('Digite Um Numero: ')),
              int(input('Digite Um Numero: ')),
                int(input('Digite Um Numero: ')))

print(f'Voce Digitou os valores {numeros}')
print(f'O Numero 9 aparece {numeros.count(9)} vezes.')
if numeros.count(3) > 0:
    posicao_3 = numeros.index(3)+1
    print(f'valor 3 apreceu na {posicao_3}° posicao')
else:
    print('O Valor 3 nao foi digitado em nenhuma posicao')
print('Os Valores Pares Digitados Pares Foram: ', end='')
for numero in range(len(numeros)):
    if numeros[numero] % 2 == 0:
        print(f'{numeros[numero]} ', end='')