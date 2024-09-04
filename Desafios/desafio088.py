# Desafio088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

mega = list()
jogo = list()
print('============= M E G A  S E N A =============')
jogos = int(input('Quantos jogos: '))
print('-'*44)
tot = 1
sleep(1)
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in mega:
            mega.append(num)
            cont += 1
        if cont >= 6:
            break
    mega.sort()
    jogo.append(mega[:])
    mega.clear()
    tot += 1
for i, l in enumerate(jogo):
    print(f'Jogo {i+1} - {l}')
    print('-' * 44)
    sleep(1)
print('                 BOA SORTE')
print('='*44)
