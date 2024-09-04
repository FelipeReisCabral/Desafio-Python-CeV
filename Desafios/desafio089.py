# Desafio089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = list()
while True:
    nome = str(input('Nome:')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    op = str(input('Continuar? [S/N]')).strip().upper()
    while op not in 'SN':
        op = str(input('Use "N" para NÃO ou "S" para SIM')).strip().upper()
    if op in 'N':
        break
    print('-'*30)
print('='*30)
print(f'{'No.':<4}{'NOME':<19}{'MÉDIA':>7}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<19}{a[2]:>7}')
print('-'*30)
aluno = int(input('Informe o No. para ver notas: [999] para parar.'))
while aluno != 999:
    print('=' * 30)
    print(f'Aluno: {ficha[aluno][0]}')
    print('-' * 30)
    print(f'''Nota 1..................: {ficha[aluno][1][0]:>4}
Nota 2..................: {ficha[aluno][1][1]:>4}
Média Final.............: {ficha[aluno][2]:>4}''')
    print('=' * 30)
    aluno = int(input('Informe o No. para ver notas: [999] para parar.'))
