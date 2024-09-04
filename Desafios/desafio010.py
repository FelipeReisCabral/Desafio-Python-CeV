# Desafio010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar. Dólar valendo = U$:3.27
r = float(input('Quantos reais você tem na carteira? '))
print('Com seus R$:{:.2f} é possivel comprar U$:{:.2f}' .format(r, r/3.27))
