# Desafio017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))
print('cateto oposto: {}\ncateto adjacente {}\nHipotenusa {:.2f}'.format(op, ad, math.hypot(op, ad)))