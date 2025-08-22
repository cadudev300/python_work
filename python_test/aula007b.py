n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
mul = n1 * n2
div = n1 / n2
di = n1 // n2
exp = n1**n2
mod = n1 % n2

print('A soma vale {} a multiplicação vale {} a divisao vale {:.3f}'.format(soma, mul, div), end = ' ')
print('A divisao inteira vale {} a potencicao vale {} eo resto da divisao vale {}'.format(di, exp, mod))