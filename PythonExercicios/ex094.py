from os import system
system('cls')
pessoas = []
pessoa = dict()
idade_media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: '))
        if pessoa['sexo'].strip()[0] in ['M', 'm', 'F', 'f']:
            break
        else:
            print('Sexo Invalido')
            

    pessoa['idade'] = int(input('Idade: '))
    print(pessoa)
    pessoas.append(pessoa.copy())
    print(pessoas)
    resp =  input('Quer Continuar[S/N]').strip()[0].upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'- O Grupo Tem {len(pessoas)} pessoas')
for pessoa in range(0, len(pessoas)):
    idade_media = idade_media + pessoas[pessoa]['idade']
idade_media = idade_media / len(pessoas)
print(f'- A media de idade é de {idade_media:.2f}')
print('- As Mulheres cadastradas foram: ', end='')
for pessoa in range(0, len(pessoas)):
    if pessoas[pessoa]['sexo'].upper() == 'F':
        print(f'{pessoas[pessoa]['nome']}', end=', ')
print('')
print('- Lista de pessoas que estao acima da media: ')
for pessoa in range(0, len(pessoas)):
    if pessoas[pessoa]['idade'] > idade_media:
        print(f'{pessoas[pessoa]['nome']};', end=' ')
        print(f'{pessoas[pessoa]['sexo']};', end=' ')
        print(f'{pessoas[pessoa]['idade']};', end=' ')
        print('')
print('\n<<ENCERRADO>>')
