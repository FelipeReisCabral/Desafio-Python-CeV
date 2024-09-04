# Desafio072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.
nome = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
numero = int(input('Digite um número de 0 - 20: '))
while True:
    if numero < 0 or numero > 20:
        numero = int(input('''Valor digitado inválido!!!
Por favor, digite um número de 0 - 20: '''))
    else:
        break
print(f'Você digitou o numero {nome[numero]}.')
