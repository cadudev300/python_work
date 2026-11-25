from os import system
import time
system('cls')
def contador(inicio, fim, passo):
    a = int(inicio)
    b = int(fim)
    c = int(passo)
    if a > b and c > 0:
        c = -c

    if a > b and c == 0:
        c = -1

    if a < b and c == 0:
        c = 1

    print('-=' * 30)
    print(f'Contagem de {a} ate {b} de {c-2*c} em {c-c-c}')
    for valor in range(int(a), int(b)+int(c), int(c)):
        
        print(valor, end=' ', flush=True)
        time.sleep(0.5)
        
    print(' FIM ')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
print('Agora e sua vez de personalizar a contagem ')
contador(input('incio: '), input('fim: '), input('passo: ')) 