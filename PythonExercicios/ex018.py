import math
angulo_graus = float(input('Informe um angulo: '))
angulo_radianos  = math.radians(angulo_graus)
print('O cos de {:.0f} ° e : {:.2f}'.format(angulo_graus, math.cos(angulo_radianos)))
print('O sin de {:.0f} ° e : {:.2f}'.format(angulo_graus, math.sin(angulo_radianos)))
print('A tangente de {:.0f} ° e : {:.2f}'.format(angulo_graus, math.tan(angulo_radianos)))