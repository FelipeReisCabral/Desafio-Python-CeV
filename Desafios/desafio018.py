# Desafio018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
ang = float(input('Digite o valor de um ângulo: '))
print('Para o ângulo de {}º teremos:\nSeno: {:.4f}\nCosseno: {:.4f}\nTangente: {:.4f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))