# Desafio065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.
opcao = 'S'
m = soma = maior = menor = 0
while opcao in 'Ss':
    num = int(input('Digite um valor inteiro: '))
    m += 1
    soma += num
    if m == 1:
        menor = maior = num
    else:
        if menor > num:
            menor = num
        if maior < num:
            maior = num
    opcao = str(input('Deseja continuar? [N/S] ')).strip()[0]
    if opcao not in 'SsNn':
        print('Opção invalida')
        opcao = str(input('Utilize as opções [N/S]: ')).strip()[0]
print('~'*30)
print('''Foram digitados {} valores
A media deles é de: {:.2f}
O maior valor digitado foi: {}
O Menor valor digitado foi: {}''' .format(m, soma/m, maior, menor))
