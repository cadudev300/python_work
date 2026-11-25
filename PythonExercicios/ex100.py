from os import system 
from time import sleep
from random import randint


system('cls')
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='\n')
    for i in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[i]}', flush=True, end=' ')
        sleep(0.3)
    print('PRONTO!')
        
def somaPar(lista):
    soma_pares = 0
    for valor in range(0, len(lista)):
        if lista[valor] % 2  == 0:
            soma_pares += lista[valor]
    print(f'Soma os valores Pares de : {lista}, temos: {soma_pares}')
#Programa Principal
numeros = []
sorteia(numeros)
somaPar(numeros)
