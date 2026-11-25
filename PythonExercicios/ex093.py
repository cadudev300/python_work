from os import system
system('cls')
jogador = {}
jogador['nome'] = str(input('Nome Do Jogador: '))
jogador['gols'] = []
jogador['total'] = 0
partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou ? '))

for i in range(0, partidas):
   jogador['gols'].append(int(input(f'Quantos Gols na Parida {i}: ')))

for v in jogador['gols']:
   jogador['total'] += v

print('=-' * 30,'\n', jogador ,'\n', '=-' * 30 )
for k, v in jogador.items():
   print(f'O Campo {k} tem o valor {v}')
print('=-' * 30)

print(f'O Jogador {jogador["nome"]} jogou {partidas} partidas')

for i in range(partidas):
   print(f'   => Na Partida {i}, fez {jogador["gols"][i]} gols')
print(f'Foi Um total de {jogador["total"]} gols. ')