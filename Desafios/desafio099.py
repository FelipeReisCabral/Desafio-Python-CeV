# Desafio099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem
# que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep


def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    if num:
        for i in range(0, len(num)):
            print(num[i], end=' ')
            sleep(0.3)
        print(f'... Foram passados {len(num)} valores e o maior valor foi {max(num)}')
    else:
        print(f'... Foram informados 0 valores.')


maior(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9))
maior(randint(0, 9))
maior()
