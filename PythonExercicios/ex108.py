from meus_modulos import moeda

p = float(input('Digite Um Preço: R$ '))
print(f'A Metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p))}')
print(f'Diminuindo 13% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p))}')