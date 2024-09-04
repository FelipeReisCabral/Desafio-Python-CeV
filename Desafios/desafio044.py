# Desafio044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
preço = float(input('Qual o preço normal do produto: R$'))
print('-='*15)
print('FORMA DE PAGAMENTO:')
print('[1] - à vista (dinheiro/cheque)')
print('[2] - à vista (cartão)')
print('[3] - 2x no cartão')
print('[4] - 3x ou mais no cartão')
op = int(input('DIGITE O Nº DA OPÇÃO: '))
print('-='*15)
if op == 1:
    preço = preço - (preço * 10 / 100)
elif op == 2:
    preço = preço - (preço * 5 / 100)
elif op == 3:
    parcela = preço / 2
    preço = preço
    print('2x de {}' .format(parcela))
elif op == 4:
    x = int(input('Quantas vezes deseja parcelar? '))
    preço = preço + (preço * 20 / 100)
    parcela = preço / x
    print('{}x de {}' . format(x, parcela))
else:
    print('OPÇÃO SELECIONADA É INVÁLIDA')
    preço = 0
print('Preço final: R${:.2f}' .format(preço))
