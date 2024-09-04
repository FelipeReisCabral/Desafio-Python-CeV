# Desafio014: Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.
temp = float(input('Informe a temperatura em ºC: '))
print('{}ºC correspondem a {}ºF'.format(temp, temp * 9 / 5 + 32))
