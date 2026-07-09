Brasileirao = (	 'Palmeiras', 
'Flamengo',
'Fluminense',
'São Paulo',
'Athletico-PR',
'Bahia',
'Bragantino',
'Vasco',
'Coritiba',
'Vitória',
'Cruzeiro',
'Botafogo',
'Atlético-MG',
'Internacional',
'Santos',
'Corinthians',
'Grêmio',
'Mirassol',
'Remo',    
'Chapecoense')
print('-='*15)
print('lista de times do Brasileirão {} '.format(Brasileirao))
print('-='*15)
print(f'Os 5 Primeirao são {Brasileirao[0:5]}')
print('-='*15)
quatro_ultimos = len(Brasileirao)- 4
print(F'4 Ultimo são {Brasileirao[quatro_ultimos::]}')
print('-='*15)
print(f'Times em ordem alfabetica {sorted(Brasileirao)}')
print('-='*15)
print(f'Chapecoense esta na {Brasileirao.index('Chapecoense')+1}° posicao.')
print('-='*15)