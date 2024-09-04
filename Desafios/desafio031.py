# Desafio031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 parta viagens mais longas.
km = int(input('Qual a distância da viagem?'))
if km <= 200:
    print('Valor da passagem: R${:.2f}' .format(km * 0.50))
else:
    print('Valor da passagem: R${:.2f}' .format(km * 0.45))
