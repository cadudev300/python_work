def notas(*notas, sit=False):
    """
    notas(*notas, sit=False)
    >> Funcao para analisar Notas e Situacões de varios Alunos.
    :param notas: Uma ou mais notas de Alunos(aceita varias).
    :param sit: Valor opcional indicando se deve ou não adicionar a situcao da turma. 
    :return: Retorna Um dicionario com varias informações sobre a turma
    """
    Notas = dict()
    soma = 0
    for i in range(0, len(notas)):
       soma = soma + notas[i]

    Notas['Tot'] = len(notas)
    Notas['Maior'] = max(notas)
    Notas['Menor'] = min(notas)
    Notas['Media'] = soma / len(notas)

    if sit == True:
        if Notas['Media'] >= 6 and  Notas['Media'] < 7:
            Notas['Situacao']  = 'RAZOAVEL'
        elif Notas['Media'] >= 7: 
            Notas['Situacao'] = 'BOA'
        elif Notas['Media'] < 6:
            Notas['Situacao'] = 'RUIM' 
    return Notas
#Programa Principal
print(notas(3.5, 2, 6.5, 2, 6, 4, sit=True ))
print(help(notas))