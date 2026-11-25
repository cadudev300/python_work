from random import randint
from time import sleep
from os import system
from operator import itemgetter
system('cls')
ranking = {"jogador1": 0, "jogador2": 0, "jogador3": 0, "jogador4": 0}
for k in ranking.keys():
    ranking[k] = randint(0, 6)
print('Valores sorteados:')
for k, v in ranking.items():
    print(f'  O {k} tirou {v}')
    sleep(0.2)
melhor_ranking = list()
melhor_ranking = sorted(ranking.items(), key=itemgetter(1), reverse=True) 

print('-='*30)
print('Ranking dos jogadores:')
for i, v in  enumerate(melhor_ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')

