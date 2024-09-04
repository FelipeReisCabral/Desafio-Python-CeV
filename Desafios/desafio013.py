# Desafio013: Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.
s = float(input('Informe o salario: R$'))
print('o salário atualizado com 15% de aumento é: R$:{:.2f}' .format(s+(s*15/100)))
