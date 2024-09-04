# Desafio085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
for i in range(1, 8):
    valor = int(input(f'Digite {i}º Valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Pares: {lista[0]}\nÍmpares: {lista[1]}')
