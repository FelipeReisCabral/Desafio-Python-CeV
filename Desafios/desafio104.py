# Desafio104: Crie um programa que tenha a função leiaInt(), que vai
# funcionar de forma semelhante ‘a função input() do Python, só que
# fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaint(num=''):
    while True:
        a = input(num)
        if a.isnumeric():
            return int(a)
        else:
            print(f'\033[31;1mERRO! digite um numero inteiro\033[m')


n = leiaint('Digite um valor: ')
print(f'Você digitou o numero \033[32;1m{n}\033[m')
