from os import system
system('clear')
valor = int(input('Informe o valor do saque : R$ '))
cedula = 0
sobra = 0
# 50, 20, 10, 1
cedula = valor // 50
sobra = valor - (cedula * 50)
valor = sobra
print(f'{cedula} cedulas de  R$ 50')
cedula = (valor // 20)
sobra = valor - (cedula * 20)
valor = sobra
print(f'{cedula} cedulas de  R$ 20')
cedula = (valor // 10)
sobra = valor - (cedula * 10)
valor = sobra
print(f'{cedula} cedulas de  R$ 10')
cedula = (sobra // 1) * 1
sobra = valor - (cedula * 1)
valor = sobra
print(f'{cedula} cedulas de  R$ 1')