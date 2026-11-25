from meus_modulos import moeda

p = float(input('Digite Um Preço: R$ '))
print(f'A Metdade de {moeda.moeda(p)} e {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.aumentar(p, True)}')
print(f'Diminuindo 13% de {moeda.moeda(p)} temos {moeda.diminuir(p, True)}')