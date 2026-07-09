from os import system
system('cls')
produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90)
print('LISTAGEM DE PREÇOS')
for cont in range(0, len(produtos), 2):
    print(f'{produtos[cont]:.<30}', end='' * 10)
    print(f'R$   {produtos[cont+1]:.2f}')
