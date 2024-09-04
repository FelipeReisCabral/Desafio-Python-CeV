# Desafio102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(x, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param x: Recebe o numero a ser fatorado
    :param show: (opcional) False = oculta a conta, True = exibe a conta.
    :return: O valor do fatorial de um nomero "x".
    """
    f = 1
    print(f'{x}!= ', end='')
    for i in range(x, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


n = int(input('Digite um número para ver o fatorial: '))
print(fatorial(n, True))
