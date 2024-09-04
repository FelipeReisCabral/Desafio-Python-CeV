# Desafio067: Faça um programa que mostre a tabuada de vários
# números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    print('='*20)
    num = int(input('Digite o valor (negativo para encerrar): '))
    print('='*20)
    if num < 0:
        break
    print(f'   TABUADA DO {num}')
    print('-'*20)
    cont = 1
    while cont <= 10:
        print(f'{num} x {cont:2} = {num * cont}')
        cont += 1
print('FIM DO PROGRAMA')
