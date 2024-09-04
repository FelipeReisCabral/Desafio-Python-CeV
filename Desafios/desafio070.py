# Desafio070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
soma = mil = menor = cont = 0
barato = ''
print('~'*26)
print('    MERCADÃO DO BAIRRO')
while True:
    print('-' * 26)
    produto = str(input('Nome do Produto: ')).strip().title()
    preço = float(input('Preço: R$'))
    cont += 1
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
      barato = produto
      menor = preço
    soma += preço
    op = str(input('Continuar? [S/N]')).strip().upper()[0]
    while op not in 'SsNn':
        op = str(input('Continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        print('=' * 26)
        print(f'''TOTAL DA COMPRA: {soma:.2f}
{mil} produtos custando mais de R$1000,00
{barato} foi o produto mais barato custando R${menor:.2f}''')
        print('-' * 26)
        break
