# Desafio069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
op = 'S'
totalidade = totalm = mulher20 = 0
print('-' * 20)
print(' CADATRO DE PESSOAS')
while True:
    if op == 'N':
        print('=' * 20)
        print(f'''Pessoas com +18: {totalidade}
Total Homens cadastrados: {totalm}
Total de mulheres -20: {mulher20}''')
        print('...\nEncerrando cadastros')
        print('=' * 20)
        break
    print('-'*20)
    idade = int(input('Idade: '))
    if idade >= 18:
        totalidade += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        totalm += 1
    if sexo == 'F' and idade <= 20:
        mulher20 += 1
    op = str(input('Continuar: [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Continuar: [S/N] ')).strip().upper()[0]
