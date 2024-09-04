# Desafio090: Faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'''
_______B O L E T I M_______
Nome: {aluno["nome"]}
Média: {aluno["media"]}''')
if aluno["media"] >= 7:
    aluno["situação"] = 'Aprovado'
elif aluno["media"] <= 5:
    aluno["situação"] = 'Reprovado'
else:
    aluno["situação"] = 'Recuperação'
print(f'Situação: {aluno["situação"]}')
print('-'*27)
