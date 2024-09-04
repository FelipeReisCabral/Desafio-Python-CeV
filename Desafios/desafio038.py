# Desafio038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
n1 = int(input('Digite o 1º numero inteiro: '))
n2 = int(input('Digite o 2º numero inteiro: '))
if n1 > n2:
    r = 'é maior que {}'.format(n2)
elif n1 < n2:
    r = 'é menor que {}'.format(n2)
elif n1 == n2:
    r = 'e {} são iguais'.format(n2)
print('O numero {} {}.' .format(n1, r))
