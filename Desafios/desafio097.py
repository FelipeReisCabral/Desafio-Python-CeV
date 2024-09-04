# Desafio097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem
# com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~~~~~~
#   Olá, Mundo!
# ~~~~~~~~~~~~~~
def escreva(msg):
    x = len(msg) + 4
    print('~' * x)
    print(f'{msg:^{x}}')
    print('~' * x)


msg = str(input('escreva algo: ')).strip().upper()
escreva(msg)
