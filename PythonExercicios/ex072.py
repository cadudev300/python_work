from os import system
system('cls')
numeros_extensos = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    while True:
        if numero > 20 or numero < 0:
            numero = int(input('Tente Novamente...Digite um numero entre 0 e 20: '))
        else:
            break
    break
print(f'Voce Digitou o numero {numeros_extensos[numero]}')
