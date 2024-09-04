# Desafio096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.
def area(l, c):
    r = l * c
    print(f'A area do terreno {l} x {c}, é de {r:.1f}m²')


print('-'*30)
print(f'{'CONTROLE DE TERRENOS':^30}')
print('-'*30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
print('-'*30)
area(largura, comprimento)
