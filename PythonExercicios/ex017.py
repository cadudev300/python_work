import math
b = float(input('Informe um valor para o cateto oposto:  '))
c = float(input('Informe um valor para o cateto adjacente: '))
a = math.sqrt(b**2 + c**2)

print('valor da hipotenusa: {:.2f}'.format(a))