from uteis_do_Cev.dados import dados
from uteis_do_Cev.moedas import moedas
p = dados.LeiaDinheiro(input('Digite Um Preço: R$ '))
#print(p)
moedas.resumo(p, 35, 22)