def ficha(jogador=0, tot_gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    if tot_gols == '':
        tot_gols = 0

    return f'O Jogador {jogador} fez {tot_gols} gol(s) no  Campeonato.'
    
#Programa Principal
nome = str(input('Nome Do jogador: '))
gols = input('Quantos Gols Ele marcou: ')

print(ficha(nome, gols))