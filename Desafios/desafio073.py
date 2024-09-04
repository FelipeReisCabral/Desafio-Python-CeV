# Desafio073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o seu time.
from time import sleep

time = ('Botafogo', 'Flamengo', 'Fortaleza', 'Palmeiras',
        'Cruzeiro', 'São Paulo', 'Bahia', 'Athletico - PR',
        'Atlético-MG', 'Bragantino', 'Vasco da Game',
        'Criciúma', 'Juventude', 'Grêmio', 'EC Vitória',
        'Internacional', 'Fluminense', 'Corinthians',
        'Cuiabá', 'Atlético-GO')
while True:
    op = int(input('''
===============================
    TABELA BRASILEIRÃO 2024
-------------------------------
[1] - Tabela completa
[2] - Os 5 primeiros colocados
[3] - Os 4 últimos colocados
[4] - Times em ordem alfabética
[5] - Descobrir posição do seu time
[0] - Sair
>>>>> Escolha a opção: '''))
    if op == 1:
        print('=' * 31)
        for pos, colocacao in enumerate(time):
            print(f'{pos + 1:2}º - {time[pos]}')
    elif op == 2:
        print('=' * 31)
        for pos in range(0, 5):
            print(f'{pos+1}º - {time[pos]}')
    elif op == 3:
        print('=' * 31)
        for pos in range(16, 20):
            print(f'{pos+1}º - {time[pos]}')
    elif op == 4:
        print('=' * 31)
        for pos in range(0, 20):
            abc = sorted(time)
            print(f'{abc[pos]}')
    elif op == 5:
        print('=' * 31)
        seu = str(input('Qual time deseja ver a posição? ')).strip().title()
        seu = time.index(seu)
        print(f'{seu + 1}º - {time[seu]}')
    elif op == 0:
        print('=' * 31)
        print('SAINDO DA APLICAÇÃO...')
        break
    sleep(1.5)
