Aluno = {}
Aluno['Nome'] = str(input('Nome: '))
Aluno['Media'] = float(input('Media: '))
if Aluno['Media'] >= 7:     
    Aluno['Situacao'] = 'Aprovado'
elif Aluno['Media'] > 5 and Aluno['Media'] < 7:
    Aluno['Situacao'] = 'recuperacao'
else:
    Aluno['Situacao'] = 'reprovado'
for k, v in Aluno.items():
    print(f'{k} é igual a {v}')