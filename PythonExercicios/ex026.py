frase = str(input('Escreva uma Frase: \n'))

print('A quantidade de letras "a" nessa frase e: {}'.format(frase.upper().count('A')))
print('A primeira aparicao de "a" fica na posicao: {}'. format(frase.upper().find('A')))
print('A ultima aparicao de "a" fica na posicao:: {}'.format(frase.upper().rfind('A')))
