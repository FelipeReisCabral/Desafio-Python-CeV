# Desafio033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
menor = n3
maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n1 < n2 and n1 < n2:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
print('{} é o maior numero.' .format(maior))
print('{} é o menor numero.' .format(menor))
