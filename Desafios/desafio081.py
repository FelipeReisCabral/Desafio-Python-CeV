# Desafio081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
cont = 0
while True:
    cont += 1
    lista.append(int(input(f'Digite o {cont}º valor: ')))
    op = str(input('Deseja continuar? [S/N]')).strip().upper()
    while op not in 'SN':
        op = str(input('Resposta inválida...[S/N]')).strip().upper()
    if op == 'N':
        lista.sort(reverse=True)
        print('-~'*30)
        print(f'A) A lista em ordem decrescente ficou: {lista}\nB) Foram digitados {len(lista)} numeros')
        if 5 in lista:
            print('C) O numero 5 está na lista.')
        else:
            print('C) Não foi digitado numero 5.')
        break
