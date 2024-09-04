# Desafio027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
nome = str(input('Digite o seu nome completo: ')).strip()
x = nome.split()
print('Nome digitado: {}\nPrimeiro Nome: {}\nÚltimo: {}'.format(nome.title(), x[0].title(), x[len(x)-1].title()))
