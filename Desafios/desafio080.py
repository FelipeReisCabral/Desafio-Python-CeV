# Desafio080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = list()
for i in range(0, 5):
    num = int(input(f'Digite o {i+1} valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        cont = 0
        while cont < len(lista):
            if num <= lista[cont]:
                lista.insert(cont, num)
                break
            cont += 1
print('-='*15)
print(lista)
