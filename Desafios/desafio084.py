# Desafio084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
lista = list()
dado = list()
pesado = leve = 0
while True:
    dado.append(str(input('Nome: ').strip().title()))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesado = leve = dado[1]
    else:
        if dado[1] > pesado:
            pesado = dado[1]
        elif dado[1] < leve:
            leve = dado[1]
    lista.append(dado[:])
    dado.clear()
    op = str(input('Continuar? [S/N]')).strip().upper()
    if op == 'N':
        print(f'A) Você cadastrou {len(lista)} pessoas.')
        print(f'B) O mais pesado tinha {pesado}Kg e se chamava', end=' ')
        for i in range(0, len(lista)):
            if pesado in lista[i]:
                print(lista[i][0], end='...')
        print(f'\nC) O mais leve tinha {leve}Kg e se chamava', end=' ')
        for i in range(0, len(lista)):
            if leve in lista[i]:
                print(lista[i][0], end='...')
        break
