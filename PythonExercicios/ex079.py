from os import system
system('cls')
numeros = []
resp = 's'
while resp in 'SsSimSIMsim':
    
    valor = int(input('Digite Um numero: '))
    if numeros.count(valor) < 1:
        numeros.append(valor) 
        print('Adicionado com Sucesso !!')
    else:
        print('Este Numero Ja foi adicionado')
    resp = str(input('Quer Continuar[S/N]: '))[0].lower().strip()
    
print(sorted(numeros))