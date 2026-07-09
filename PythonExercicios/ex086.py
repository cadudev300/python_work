matriz = [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite Um Numero: '))

for linha in range(0, len(matriz)):
    for coluna in range(0, 3):
        print(f' [{matriz[linha][coluna]:^5}]', end='')
    print()
#print(matriz)