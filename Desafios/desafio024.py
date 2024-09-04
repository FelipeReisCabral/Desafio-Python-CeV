# Desafio024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = input('Digite o nome de uma cidade:' ).strip()
x = cidade.lower()
z = x.split()
print('Está cidade começa com a palavra Santo? {}' .format('santo' in z[0]))
