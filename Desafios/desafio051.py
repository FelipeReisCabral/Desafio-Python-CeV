# Desafio051: Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão.
termo = int(input('Informe o primeiro termo da PA:'))
razao = int(input('Informe a razão da PA: '))
decimo = termo + (10 -1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end='-')
print('FIM')
