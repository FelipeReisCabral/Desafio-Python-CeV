# Desafio078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
for i in range(1, 6):
    valores.append(int(input(f'Digite {i}º valor:')))
print('=#'*30)
print(f'A lista de valores digitados foi: {valores}')
print(f'O maior valor digitado foi {max(valores)} e apareceu nas posições: ', end='')
for v, i in enumerate(valores):
    if i == max(valores):
        print(f'{v}...', end='')
print(f'\nO menor valor digitado foi {min(valores)} e apareceu nas posições: ', end='')
for v, i in enumerate(valores):
    if i == min(valores):
        print(f'{v}...', end='')
