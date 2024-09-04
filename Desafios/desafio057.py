# Desafio057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
r = str(input('Informe o seu sexo [M/F]:')).strip()[0]
while r not in 'MmFf':
    r = str(input('Opção invalida!!! Informe o seu sexo corretamente [M/F]:')).strip()[0]
if r in 'Mm':
    r = 'Masculino'
elif r in 'Ff':
    r = 'Feminino'
print('Você é do sexo {}.' .format(r))
