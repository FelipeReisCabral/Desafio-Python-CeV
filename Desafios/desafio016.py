#Desafio016: Crie um programa que leia um número Real qualquer pelo teclado e
# mostre na tela a sua porção Inteira.
import math
num = float(input('Digite um numero real: '))
print('a parte inteira do numero {} é {}'.format(num, math.trunc(num)))
