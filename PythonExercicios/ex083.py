from os import system
system('cls')
parenteses = []
# lendo uma expressao 
expressao = str(input('Digite Uma Expressão: '))
# percorrendo cada caracter da lista
for caracter in expressao:
    # guardando o na lista 'parenteses' se o caracter for um parenteses 
    if caracter == '(' or caracter == ')':
        parenteses.append(caracter)

if parenteses.count('(') == parenteses.count(')'):
    print('Sua Expressão esta Correta !!!')
else:
    print('Sua Expressão está errada !!!') 

# exibindo a lista parenteses
# print(f'{parenteses}')