from time import sleep
from os import system

system('cls')
def HelpPy():
    while True:

        print('\033[44m~' * 23 + ' ')
        print(' SISTEMA DE AJUDA PyHELP')
        print('~' * 23 + ' \33[0m')

        comando = input('Função ou Bibioteca: ')
        if comando in 'fim Fim f':
            print('='*10)
            print('\033[48m ATÉ LOGO')
            print('='*10)
            break
        else:
            print('--' * 20)
            print(f'\033[22mAcessando manual do comando {comando} \033[0m')
            print('--' * 20)
            sleep(2/4)
            print('\033[34m')
            help(comando)

HelpPy()