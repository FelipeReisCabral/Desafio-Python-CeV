# Desafio058: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no
# final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep

cont = 0
print('-=-'*20)
print('Vou pensar em um numero de 0 a 10 e você tenta adivinhar...')
print('-=-'*20)
for c in range (1, 4):
    sleep(0.5)
    print('.', end="")
palp = int(input('Tente adivinhar o valor: '))
num = randint(0, 10)
for c in range (1, 4):
    sleep(0.5)
while palp != num:
    if palp < num:
        palp = int(input('Errou, é mais. Tente denovo: '))
        cont += 1
    elif palp > num:
        palp = int(input('Errou, é menos. Tente denovo: '))
        cont += 1
if cont == 0:
    print('ACERTOU!! de primeira, incrivel.')
else:
    print('Acertou!! depois de {} tentativas.' . format(cont+1))
