def area(l, c):
    a = l * c
    print('Controle de Terrenos')
    print(f'a area de um terreno de {l} x {c} é de {a}m²')


#Programa Principal
largura = float(input('Largura (m):'))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)