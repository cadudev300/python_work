from os import system
system('cls') 
numeros = []
for contador in range(1, 6):
    if contador == 1:
        valor = int(input('Digite Um Numero: '))
        numeros.insert(-1, valor)
        print(f'{valor} Adicionado ao Final da lista')
    else:
        valor = int(input('Digite Um Numero: '))
        ultimo_valor = numeros[-1]
        if valor > ultimo_valor:
            numeros.append(valor)
            print(f'{valor} adicionado final da lista')
        elif valor < ultimo_valor and len(numeros) < 2:
            numeros.insert(0, valor)
            print('Adicionado na Posicao 0 da lista')
        else:
            for contador in range(0, len(numeros)):
                if valor < numeros[contador]:
                    numeros.insert(contador, valor)
                    print(f'Adicionado na posicao {contador}° da lista ')
                    break
print(numeros)