# Desafio043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
peso = float(input('Informe o seu peso:'))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif imc < 25:
    status = 'PESO IDEAL'
elif imc < 30:
    status = 'SOBREPESO'
elif imc < 40:
    status = 'OBESIDADE'
else:
    status = 'OBESIDADE MÓRBIDA'
print('IMC: {:.2f}\nStatus: {}' .format(imc, status))
