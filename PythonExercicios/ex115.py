from sistema_de_cadastros import sistema
from os import system
system('cls')
while True:
    print('\033[33m-'*30)
    print('MENU PRINCIAPL'.center(30))
    print('-'*30)
    print('\033[32m1-VER PESSOAS CADASTRADAS.')
    print('2-CADASTRAR UMA NOVA PESSOA')
    print('3-SAIR DO SISTEMA')
    try:
        opcao = int(input('Sua Opção: '))
    except(ValueError):
        print('\033[31mERRO: por favor digite uma opção válida...\033[m')
        continue


    if opcao == 1:
        sistema.pessoas_cadastradas()
    elif opcao == 2:
        sistema.pessoas_cadastros()
    elif opcao == 3:
        print('='*30)
        print('Saindo do sitema')
        print('='*30)
        break
    else:
        print('\033[31m ERRO: por favor digite uma opção válida...\033[m')
        continue