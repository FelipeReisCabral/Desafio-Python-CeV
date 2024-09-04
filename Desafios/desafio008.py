# Dasafio008: Escreva um programa que leia um valor em metros e o exiba convertido em
# centímetros e milímetros.
medida = float(input('Digite uma medida em metros: '))
print('a medida {}mts equivalem a {:.2f}cm e {:.2f}mm' .format(medida, medida*100, medida*1000))
