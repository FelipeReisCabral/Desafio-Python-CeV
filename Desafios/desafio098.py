# Desafio098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que
# realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def cont(a, b, c):
    for v in range(a, b, c):
        print(v, end=' ')
        sleep(0.3)
    print(f'FIM!')


print('-=' * 20)
print(f'Contando de 1 até 10 de 1 em 1:')
cont(1, 11, 1)
print('-=' * 20)
print(f'Contando de 10 até 1 de 2 em 2:')
cont(10, -1, -2)
print('-='*20)
print('Personalize a sua contagem: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 20)
if passo == 0:
    passo = 1
    if inicio < fim:
        print(f'Contando de {inicio} até {fim} de {passo} em {passo}:')
        fim += 1
        cont(inicio, fim, passo)
    elif inicio > fim:
        print(f'Contando de {inicio} até {fim} de {passo} em {passo}:')
        fim -= 1
        cont(inicio, fim, -passo)
elif passo < 0:
    print(f'Contando de {inicio} até {fim} de {passo*-1} em {passo*-1}:')
    fim -= 1
    cont(inicio, fim, passo)
else:
    if inicio < fim:
        print(f'Contando de {inicio} até {fim} de {passo} em {passo}:')
        fim += 1
        cont(inicio, fim, passo)
    elif inicio > fim:
        print(f'Contando de {inicio} até {fim} de {passo} em {passo}:')
        fim -= 1
        cont(inicio, fim, -passo)
