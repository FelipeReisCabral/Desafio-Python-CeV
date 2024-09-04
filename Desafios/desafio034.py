# Desafio034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os
# inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual o salário? R$'))
if sal > 1250:
    print('Seu novo salário com o aumento de 10% será: R${:.2f}' .format(sal + (sal * 10 / 100)))
else:
    print('Seu novo salário com o aumento de 15% será: R${:.2f}' .format(sal + (sal * 15 / 100)))
