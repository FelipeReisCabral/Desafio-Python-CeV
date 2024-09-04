# Desafio036: Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado.
print('-='*12)
print('ANALIZADOR DE EMPRESTIMO')
print('-='*12)
casa = float(input('Qual o valor do imóvel: R$'))
salario = float(input('Qual o valor do salário: R$'))
tempo = int(input('Quantos anos para pagar? '))
mes = tempo * 12
prestacao = casa / mes
if prestacao < (salario*30/100):
    print('Valor da prestação: R${:.2f}\nNumero de prestações: {} vezes' .format(prestacao, mes))
else:
    print('O valor excede 30% do seu salário\nNão é possivel fazer o empréstimo.')
