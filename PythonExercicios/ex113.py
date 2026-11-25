while True:
    try:
        valor_inteiro = int(input('Digite Um Valor Inteiro:'))
    except (ValueError, TypeError ):
        print('ERRO: Tipo de dado não válido digite novamente')
        continue
    except(KeyboardInterrupt, EOFError, NameError):
        print(f'O USUARIO PREFERIU NAO DIGITAR ESTE NÚMERO')
        valor_inteiro = 0 
        print(f'O valor inteiro foi {valor_inteiro}')
        break
    else:
        break

while True:
    try:
        valor_real = float(input('Digite Um Valor real:'))
    except (ValueError, TypeError):
        print('ERRO: Tipo de dado não válido digite novamente')
        continue
    except(KeyboardInterrupt, EOFError, NameError):
        print(f'O USUARIO PREFERIU NAO DIGITAR ESTE NÚMERO')
        valor_real = 0 
        print(f'O valor real foi {valor_real}')
        break
    else:
        break

print(f'Valor Inteiro foi {valor_inteiro} e o Valor Real foi {valor_real}')