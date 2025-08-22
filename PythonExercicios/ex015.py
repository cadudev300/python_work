
dias_alugados = int(input('Quantos dias alugados? '))
km_percorridos = float(input('Quantos Km rodados? '))
preco_total = (dias_alugados*60) + (km_percorridos*0.15)

print('O total a pagar e R$ {:.2f}'.format(preco_total))
