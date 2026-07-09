from os import system
system('cls')
contador = 0
palavras = ['APRENDER', 'PRATICAR', 'TRABALHAR', 'ESTUDAR', 'PROGRAMADOR', 'FUTURO', 'MERCADO']
for palavra in palavras:
    print(f'NA PALAVRA {palavra} temos ', end='')
    for letra in palavra:
        if letra in ('A', 'E', 'I', 'O', 'U'):
           print(letra,end=' ')
    print()
