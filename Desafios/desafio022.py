# Desafio022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras no total (sem considerar espaços).
# – Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em upper: {}' .format(nome.upper()))
print('Nome em lower: {}' .format(nome.lower()))
cont = nome.split()
tot = ''.join(cont)
print('Total de letras sem espaço: {} letras'.format(len(tot)))
print('Total de letras do primeiro nome: {} letras' .format(len(cont[0])))
