# Desafio060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Informe um numero: '))
f = n
print('{}! = ' .format(n), end='')
while n > 1:
    print(n, 'x', end=' ')
    n -= 1
    f = f * n
print('1 = {}'.format(f))
