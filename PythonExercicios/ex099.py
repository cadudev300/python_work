from os import system
from time import sleep
from random import randint
def maior(*valores):
    maior_valor = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i in range(len(valores)): 
        print(f'{valores[i]}',flush=True, end=' ' )
        sleep(0.4)
        if valores[i] == 0:
            maior_valor = valores[i]
        if valores[i] > maior_valor:
            maior_valor = valores[i]

    print(f'Ao todo foi informado {len(valores)} valores')
    print(f'O Maior valor informado foi: {maior_valor} ')
    
#Programa Principal
system('cls')
maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(7, 43, 54, 2)
maior(9, 16, 4, 8)
maior(6)
maior()