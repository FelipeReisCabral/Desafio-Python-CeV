# Desafio082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e
# os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.
lista = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    op = str(input('Deseja continuar: [S/N]')).strip().upper()
    while op not in 'SN':
        op = str(input('Opção inválida, Digite "S" para continuar ou "N" para sair.')).strip().upper()
    if op == 'N':
        break
par = list()
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
impar = list()
for i, v in enumerate(lista):
    if v % 2 != 0:
        impar.append(v)
print(f'Os valores digitados foram {lista}\nOs numeros pares foram: {par}\nOs numeros impares foram{impar}')
