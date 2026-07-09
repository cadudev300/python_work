
alunos = []
while True:
    Nome = str(input('Nome: '))
    Nota1 = float(input('Nota 1: '))
    Nota2 = float(input('Nota 2: '))
    media = (Nota1 + Nota2) / 2
    alunos.append([Nome, Nota1, Nota2, media])
    resp = input('Quer Continuar [S/N]: ')
    if resp.strip()[0] in 'Nn':
        break
print(f'Nomes:     Medias:')
for valor in range(0, len(alunos)):
    # exibindo Nome de cada Aluno e sua media
    print(f'{valor} {alunos[valor][0]:<10}    {alunos[valor][3]: <10}')
while True: 
    notas = int(input('Quer Ver as Notas de qual Aluno [999] para encerrar...'))
    if notas == 999:
        break
    if notas <= len(alunos):
        print(alunos[notas][1], alunos[notas][2])