# Desafio039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é
# a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
idade = int(input('Qual o ano de seu nascimento? '))
sexo = int(input('''Qual seu sexo:
[1] - HOMEM
[2] - MULHER
Digite a opção: '''))
idade = date.today().year - idade
if sexo == 1:
    if idade == 18:
        print('Já está na hora de se alistar no exército pequeno gafanhoto.')
    elif idade < 18:
        print('Fique atento, faltam {} anos para você se alistar ao exército.' .format(18 - idade))
    elif idade > 18:
        print('Com {} anos, já passou o tempo para você se alistar'.format(idade - 18))
elif sexo ==2:
    print('Você não precisa se alistar.')
