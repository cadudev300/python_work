def voto(ano_nasc=0):
    global ano_atual
    idade = ano_atual - ano_nasc
    if idade >= 18 and idade < 65 :
        return f'COM {idade} ANOS: VOTO OBRIGATORIO !!'
    elif idade <= 16:
        return f'COM {idade} ANOS: VOTO NEGADO !!'
    elif idade>= 65 or idade >= 16:
        return f'COM {idade} ANOS: VOTO OPCIONAL !!'


#Programa Principal
ano_atual = 2026
ano_nacimento = int(input('Digite seu Ano de nacimento: '))
print(voto(ano_nacimento))