# Desafio03: Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.
l1 = float(input('Digite o comprimento do 1º lado: '))
l2 = float(input('Digite o comprimento do 2º lado: '))
l3 = float(input('Digite o comprimento do 3º lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Com as medidas dos lados {} x {} x {} é possivel formar um triângulo.' .format(l1, l2, l3))
else:
    print('Com as medidas dos lados {} x {} x {} NÃO é possivel formar um triângulo.' .format(l1, l2, l3))
