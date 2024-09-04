# Desafio056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do
# homem mais velho e quantas mulheres têm menos de 20 anos.
maior = 0
menor = 0
soma = 0
for i in range(0, 4):
    nome = str(input('Digite o nome: ')).strip().title()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).strip().upper()
    if idade > maior and sexo == 'M':
        velho = nome
        maior = idade
    elif idade < 20 and sexo == 'F':
        menor = menor + 1
    soma = soma + idade
print('A media de idade do grupo é de {:.2f} anos' . format(soma/4))
print('O {} é o homem mais velho com {} anos' .format(velho, maior))
print('A quantidade de mulheres com menos de 20 anos: {}' . format(menor))
