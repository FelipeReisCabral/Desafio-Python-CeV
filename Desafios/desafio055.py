# Desafio055: Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.
for i in range(1, 6):
    peso = float(input('Digite  peso em Kg: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior Peso: {}Kg\nMenor Peso: {}Kg' .format(maior, menor))
