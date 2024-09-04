# Desafio068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vit = 0
while True:
    num = int(input('Digite um valor: '))
    op = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    cpu = randint(0, 10)
    resultado = num + cpu
    print('~'*20)
    print(f'''Você escolheu: {'PAR' if op == 'P' else 'ÍMPAR'}
Você jogou: {num}
Computador jogou: {cpu}''')
    if op == 'P':
        if resultado % 2 == 0:
            print(f'Total: {resultado} é PAR... \033[1;32mVocê venceu\033[m!')
            vit += 1
        else:
            print(f'Total: {resultado} é ÍMPAR... \033[1;31mComputador venceu\033[m!')
            print('=' * 20)
            print(f'''FIM DE JOGO
Você venceu {vit} vezes.''')
            print('=' * 20)
            break
    elif op == 'I':
        if resultado % 2 > 0:
            print(f'Total: {resultado} é ÍMPAR... \033[1;32mVocê venceu\033[m!')
            vit += 1
        else:
            print(f'Total: {resultado} é PAR... \033[1;31mComputador venceu\033[m')
            print('=' * 20)
            print(f'''FIM DE JOGO
Você venceu {vit} vezes.''')
            print('=' * 20)
            break
    print('~' * 20)
