import time
from os import system
from random import randint
system('cls')
print('-- JOGO DA MEGA SENA --')
quant_jogos = int(input('Quantos Jogos Quer que eu sorteie ? '))
palpites = []
for i in range(0, quant_jogos):
    palpites.append([])
for lista in range(0, len(palpites)):
    for i in range(0, 6):
        while True:
            numero = randint(0, 60)
            if numero not in palpites[lista]:
                palpites[lista].append(numero)
                break
            else:
                continue

    print(f'Jogo {lista} : {palpites[lista]}')
    time.sleep(0.5)
print('--- BOA SORTE !!! ---')
