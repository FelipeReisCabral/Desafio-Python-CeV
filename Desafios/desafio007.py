# Dasafio007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = input('Nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('Nome: {} \nPrimeira nota: {} \nSegunda nota: {} \nMedia final: {:.2f}' .format(nome, n1, n2, (n1+n2)/2))
