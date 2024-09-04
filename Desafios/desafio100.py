# Desafio100: Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
# valores pares sorteados pela função anterior.
from random import randint
from time import sleep

lista = list()


def sorteia():
    print('Sorteando 5 números aleatórios: ', end='')
    for i in range(0, 5):
        num = randint(0, 9)
        print(num, end=' ')
        lista.append(num)
        sleep(0.5)
    print('\nValores adicionas numa lista: ', lista)
    print('~'*46)


def somapar(lst):
    soma = 0
    print('Os valores pares na lista : ', end='')
    for num in lst:
        if num != 0:
            if num % 2 == 0:
                sleep(0.5)
                print(num, end=' ')
                soma += num
    print(f'\nA soma total deles é igual a {soma}')
    print('~' * 46)


sorteia()
somapar(lista)
