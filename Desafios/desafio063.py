# Desafio063: Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
i = int(input('Digite um numero:'))
c = 0
f1 = 0
f2 = 1
print('{} - {}'.format(f1, f2), end=' - ')
while c < i - 3:
    f3 = f2 + f1
    f1 = f2
    f2 = f3
    print('{} - '.format(f3), end='')
    c += 1
print(f1+f2, '- FIM')
