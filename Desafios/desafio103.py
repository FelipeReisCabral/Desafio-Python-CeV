# Desafio103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos
# gols ele marcou. O programa deverá ser capaz de mostrar a ficha do
# jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(a='', b=''):
    """
    :param a: Recebe o nome de um jogador, caso não infomado retorna <desconhecido>
    :param b: Recebe o numero de gols, caso não informado retorna "0"
    :return: Retorna uma msg formatada informando o nome do jogador e o numero de gols dele no campeontado
    """
    if a == '':
        a = '<desconhecido>'
    if b == '' or b.isalpha():
        b = 0
    else:
        b = int(b)
    return f'O Jogador {a} fez {b} gol(s) no campeonato'


nome = str(input('Nome do jogador: ')).strip().title()
gols = str(input('Nº de gols: '))
print(ficha(nome, gols))
