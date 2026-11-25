def fatorial(num, show=False):
    """
    fatorial(num, show=False)
    >> Calcula o fatorial de um numero.
    :param: n: O numero a ser calculado.
    :param: show: (opcional) Mostrar ou Não o Calculo Fatorial.
    :return: O Valor fatorial de um numero n.
    """
    f = 1
    for contador in range(num, 1, -1):
        f = f * contador

    if show == True:
        for cont in range(num, 0, -1):
            print(f' {cont} ', end='')
            if cont != 1:
               print(' x ', end='')

        print(' = ', end='')
    return f


#programa principal
n = 5
print(fatorial(6, show=True))
help(fatorial)