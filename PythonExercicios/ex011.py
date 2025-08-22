largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
area = largura*altura
print(f'valor da area: {area} m²')
print('Sabendo que cada litro de tinta pinta 2 m² ')
print('A quantidade de tinta necessaria para píntar uma area de {} m² \nequivale a: {:.2f} litros '.format(area, area/2))