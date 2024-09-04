# Desafio076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
# preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Arroz', 5.49, 'Carne', 17.89, 'Farinha', 3.85, 'Açucar', 4.89, 'Sal', 2.50, 'Ovos', 12.00,
         'Oleo', 8.00, 'Fermento', 1.50, 'Lentilha', 6.99, 'Café', 14.98, 'Leite', 4.49, 'Manteiga',
         9.99, 'Macarão', 2.90)
i = 0
titulo = 'LISTAGEM DE PREÇOS'
print('-'*40)
print(f'{titulo:^40}')
print('-'*40)
while i < len(lista):
    print(f'{lista[i]:.<30} R$', end='')
    print('{:.2f}'.format(lista[i+1]).rjust(6))
    i += 2
print('-'*40)
