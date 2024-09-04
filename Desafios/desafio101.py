# Desafio101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(a):
    from datetime import date
    ano = date.today().year - a
    if ano == 16 or ano == 17 or ano >= 70:
        return f'Com {ano} anos o voto é FACULTATIVO'
    elif ano < 16:
        return f'Com {ano} anos NÃO pode votar'
    else:
        return f'Com {ano} anos o voto é OBRIGATÓRIO'


def titulo():
    titulo = 'ANALISADOR DE VOTOS'
    print('-'*40)
    print(f'{titulo:^40}')
    print('-='*20)


titulo()
ano = int(input('Informe o ano de nascimento:'))
print(voto(ano))
