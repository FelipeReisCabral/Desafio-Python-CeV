# Desafio054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

maior = 0
menor = 0
for i in range(0, 7):
    nasc = int(input('Digite o ano de nascimento (yyyy): '))
    idade = date.today().year - nasc
    if idade >= 21:
        maior = maior + 1
    elif idade < 21:
        menor = menor + 1
print('RESULTADO:\nMaiores de 21 anos: {} pessoas\nMenores de 21 anos: {} pessoas' .format(maior, menor))
