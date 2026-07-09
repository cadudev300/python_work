numeros = []

for contador in range(0, 5):
    numeros.append(float(input(f'Digite Um Numero para a posicao {contador} ')))
maior = max(numeros)
menor = min(numeros)
print(f'Voce Digitou os valores {numeros} ')
print(f'O Maior valor foi {maior} nas posicoes: ', end='')
for chave, valor in enumerate(numeros):
    if maior == valor:
        print(f'{chave}... ', end='')

print(f'\nO Menor valor foi {menor} nas posicoes: ', end='')
for chave, valor in enumerate(numeros):
    if menor == valor:
        print(f'{chave}... ', end='')
