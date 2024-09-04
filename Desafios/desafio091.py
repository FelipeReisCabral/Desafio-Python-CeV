# Desafio091: Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

lista = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)
         }
ranking = list()
print('Valores sorteados')
for k, v in lista.items():
    print(f'{k} tirou o número {v}')
    sleep(1)
ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)
print('=+'*15)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
