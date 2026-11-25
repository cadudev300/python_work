from meus_modulos import moeda

p = float(input('Digite Um Preço: R$ '))
print(f'A Metdade de {p} e {moeda.metade(p)}')
print(f'O dobro de {p} e {moeda.dobro(p)}')
print(f'Aumentando 10% de {p} temos {moeda.aumentar(p)}')
print(f'Diminuindo 13% de {p} temos {moeda.diminuir(p)}')