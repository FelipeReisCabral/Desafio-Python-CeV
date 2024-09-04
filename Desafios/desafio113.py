# Desafio113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo
# inválido. Aproveite e crie também uma função leiaFloat() com a mesma
# funcionalidade.
from funcoes.desafio113 import *

a = leiaInt('Digite um valor inteiro: ')
b = leiaReal('Digite um valor Real: ')
print(f'A valor inteiro foi {a} e o real foi {b}')
