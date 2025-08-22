from random import shuffle
aluno_1 = input('Informe o nome no primeiro aluno: ')
aluno_2 = input('Informe o nome no segundo aluno: ')
aluno_3 = input('Informe o nome no terceiro aluno: ')
aluno_4 = input('Informe o nome no quarto aluno: ')
lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_alunos)
print('--' * 12)
print('A ordem de apresentação sera:')
print(lista_alunos)