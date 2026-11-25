from os import system
system('cls')
jogadores = list()
jogador = {}
while True:
   #jogador.clear()
    jogador['nome'] = str(input('Nome Do Jogador: '))
    jogador['gols'] = []
    jogador['total'] = 0
    partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou ? '))

    for i in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos Gols na Parida {i}: ')))

    for v in jogador['gols']:
        jogador['total'] += v
    jogadores.append(jogador.copy())
    
    resp = input('Quer Continuar[S/N]: ')
    if resp.strip()[0].upper() == 'N':
        break

print('-=' * 30)
for j in range(0, len(jogadores)):
   print(f'{j} {jogadores[j]["nome"]:^15} {jogadores[j]["gols"]} {jogadores[j]["total"]:^15}')
#c = 0

while True:
    dados = int(input('Mostrar dados de qual jogador?'))
    if dados == 999:
        break
    elif dados > len(jogadores) or dados < 0:
        print('Jogador Nao Encontrado')  
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}')
        for jogo in range(0, len(jogadores[dados]['gols'])):
            print(f'No jogo {jogo} ele fez {jogadores[dados]["gols"][jogo]}')

