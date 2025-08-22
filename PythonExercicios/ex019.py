import random
aluno_1 = input('Informe o nome no primeiro aluno: ')
aluno_2 = input('Informe o nome no segundo aluno: ')
aluno_3 = input('Informe o nome no terceiro aluno: ')
aluno_4 = input('Informe o nome no quarto aluno: ')

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
aluno_escolhido = random.choice(lista_alunos)
print('O aluno escolhido foi {} '.format(aluno_escolhido))
