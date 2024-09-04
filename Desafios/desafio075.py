# Desafio075: Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
n = (int(input('Digite 1o um valor: ')),
     int(input('Digite 2o um valor: ')),
     int(input('Digite 3o um valor: ')),
     int(input('Digite 4o um valor: ')))
print(f'Você digitou os valores {n}')
print(f'O numero 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro numero 3 apareceu na posição {n.index(3)+1}º')
else:
    print('Não foram digitados numero 3 na sequência.')
print('Os numeros pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
