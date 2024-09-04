# Desafio059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
opcao = 0
while opcao != 5:
    print('''------------M-E-N-U------------
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Números
    [5] - Sair do Programa
-------------------------------''')
    opcao = int(input('>>> Escolha a opção:'))
    if opcao == 1:
        print('A soma dos dois números informados é: {}' .format(n1 + n2))
    elif opcao == 2:
        print('A multiplicação dos dois números informados é: {}' .format (n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} é o maior número digitado. ' .format(n1))
        else:
            print('{} é o maior número digitado. ' .format(n2))
    elif opcao == 4:
        n1 = int(input('Informe um novo valor para substituir o valor {}: ' .format(n1)))
        n2 = int(input('Informe um novo valor para substituir o valor {}: ' .format(n2)))
    elif opcao == 5:
        print('SAINDO...')
    else:
        print('OPÇÃO INVÁLIDA, ESCOLHA NOVAMENTE')
