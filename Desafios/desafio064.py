# Desafio064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando o flag).
n = soma = c = 0
n = int(input('Digite um numero inteiro ([999] para sair): '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um numero inteiro ([999] para sair): '))
print('Foram digitados {} Numeros, a Soma deles foi igual a {}'.format(c, soma))
