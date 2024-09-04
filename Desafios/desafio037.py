# Desafio037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite o numero a ser convertido:'))
print('-'*30)
opcao = int(input('[1] Binário\n[2] Octal\n[3] Hexadecimal\nEscolha qual a base desejada: '))
print('-'*30)
if opcao == 1:
    base = bin(num)[2:]
    opcao = 'Binário'
    print('O numero {} convertido para a base {} é: {}'.format(num, opcao, base.upper()))
elif opcao == 2:
    base = oct(num)[2:]
    opcao = 'Octal'
    print('O numero {} convertido para a base {} é: {}'.format(num, opcao, base.upper()))
elif opcao == 3:
    base = hex(num)[2:]
    opcao = 'Hexadecimal'
    print('O numero {} convertido para {} é: {}'.format(num, opcao, base.upper()))
else:
    print('Opção inválida...')
