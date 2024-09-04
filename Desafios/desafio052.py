# Desafio052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um numero: '))
i = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end='')
        i += 1
    else:
        print('\033[31m', end='')
    print('{}\033[m, ' .format(c), end='')
print('\033[mFIM\nO número {} foi divisivel {} vezes.' .format(n, i))
if i == 2:
    print('Por esse motivo ele é PRIMO')
else:
    print('por isso NÃO é primo')
