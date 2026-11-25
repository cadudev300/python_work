def LeiaInt(text):
    while True:
        num = input(f'{text}')
        try:
            num = int(num)
        except:
            print('ERRO ! Digite Um Numero Inteiro Válido')
            while True:
                num = input(f'{text}')
                try:
                    num = int(num)
                    break
                except:
                    print('ERRO ! Digite Um Numero Inteiro Válido')
                    continue
        break
    return num 

#Programa Principal
n = LeiaInt('Digite Um Numero:')
print(f'Você Acabou de digitar o número {n}')
