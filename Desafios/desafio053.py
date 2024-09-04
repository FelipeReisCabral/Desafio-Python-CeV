# Desafio053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

# Exemplos:
# APOS A SOPA, A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).strip().lower()
res = frase
frase = frase.split()
frase = ''.join(frase)
letras = len(frase)
p = 0
for c in range(0, len(frase)):
    letras = letras - 1
    if frase[c] == frase[letras]:
        p = p + 1
        if p == len(frase):
            print('A frase "{}", é um PALÍNDROMO'.format(res.title()))
if p != len(frase):
    print('A frase "{}", NÃO é um palíndromo.' .format(res.title()))
