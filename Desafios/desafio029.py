# Desafio029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
# multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Qual a velocidade do carro?'))
dif = vel - 80
if vel > 80:
    print('Você passou {}Km acima do permitido, sua multa será de R${:.2f}'.format(dif, dif * 7.00))
else:
    print('Velocidade dentro do permitido!')