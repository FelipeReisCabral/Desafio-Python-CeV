# Desafio006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
x = int(input('Digite um numero: '))
print('O valor digitado é: {} \nO dobro dele é: {} \nO triplo dele é: {} \nA raiz quadrada é: {:.2f}' .format(x, x*2, x*3, x**(1/2)))
