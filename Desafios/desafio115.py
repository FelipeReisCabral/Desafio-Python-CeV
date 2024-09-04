# Desafio115a: Vamos criar um menu em Python, usando modularização.
# Desafio115b: Vamos ver como fazer acesso a arquivos usando o Python.
# Desafio115c: Vamos finalizar o projeto de acesso a arquivos em Python.
from funcoes.desafio115 import *

while True:
    menuprincipal()
    op = opcao(f'{cores(5)}Sua opção:{cores(0)} ')
    if op == 3:
        break
