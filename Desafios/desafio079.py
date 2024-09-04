# Desafio079: Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
num = list()
while True:
    valor = int(input(f'Digite um valor:'))
    if valor in num:
        print('Valor duplicado, não foi possivel adicionar.')
    else:
        num.append(valor)
    op = (str(input('Adicionado com sucesso... continuar? [S/N]'))).upper().strip()
    while op not in 'SN':
        op = str(input(f'Valor "{op}" é inválido: Use "S" para SIM ou "N" para NÃO.')).strip().upper()
        if op == 'N':
            break
    if 'N' in op:
        num.sort()
        print('-='*25)
        print(f'A lista de valores digitados foi {num}')
        break
