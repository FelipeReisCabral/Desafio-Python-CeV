# Desafio011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a
# sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2 metros quadrados.
h = float(input('Informe a altura da parede em metros: '))
c = float(input('Informe a largura da parede em metros: '))
m = h*c
print('A area total de uma parede com {:.2f}mt de altura e {:.2f}mt de largura é {:.2f}m² \nPara este tamanho de parede será necessario {:.2f} litros de tinta para pintar.' .format(h, c, m, m/2))
