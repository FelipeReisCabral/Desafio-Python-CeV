# Desafio020:  O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a
# ordem sorteada.
import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista)
