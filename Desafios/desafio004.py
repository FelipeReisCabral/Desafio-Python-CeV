# Desafio004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele.
x = input('Digite algo:')
print('Tipo primitivo:', type(x))
print('Só tem espaços? ', x.isspace())
print('É alphanumeric? ', x.isalnum())
print('É alphabetic? ', x.isalpha())
print('É um ASCII? ', x.isascii())
print('É um dígito? ', x.isdigit())
print('Está em caixa baixa? ', x.islower())
print('Está em caixa alta? ', x.isupper())
print('Está em capitalizada? ', x.istitle())
print('É um número? ', x.isnumeric())
