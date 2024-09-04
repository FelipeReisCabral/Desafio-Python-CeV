# Desafio028:  Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
# computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

print('-=-'*20)
print('Vou pensar em um numero de 0 a 5 e você tenta adivinhar...')
print('-=-'*20)
sleep(0.5)
print('.')
sleep(0.5)
print('.')
palp = int(input('Tente adivinhar o valor: '))
num = random.randint(0, 5)
if palp == num:
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    print('Meu deus, como você adivinhou que era {}?!?!?!'.format(palp))
else:
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    print('Errou!!! O número era {} e não {}. Eu venci, mas a tentativa foi boa!!'.format(num, palp))
