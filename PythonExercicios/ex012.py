valor = float(input('Informe o valor do produto R$ '))
desconto = (5 * valor) /100
valor_descontado = valor - desconto
print('produto que custava {} com desconto de 5% vai custar  R$ {}'.format(valor, valor_descontado) )