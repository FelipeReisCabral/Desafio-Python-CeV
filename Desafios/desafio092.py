# Desafio092: Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for
# diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
dados['nasc'] = int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho: [0 para N/A]'))
dados['idad'] = date.today().year - dados['nasc']

if dados['ctps'] != 0:
    dados['cont'] = int(input('Ano de contratação: '))
    dados['sala'] = float(input('Salário: R$'))
    dados['apos'] = date.today().year - dados['cont']
    if dados['apos'] > 35:
        status = 'APOSENTADO'
    elif dados['apos'] == 35:
        status = 'Se aposenta este ano'
    else:
        aposentadoria = 35 - dados['apos']
        status = f'Faltam {aposentadoria} anos de contribuição.'
    print(f'''
------------FICHA DO TRABALHADOR------------

Nome: {dados['nome']}
Ano de Nasc.: {dados['nasc']:<4}            Idade: {dados['idad']}
Nº. CTPS: {dados['ctps']}

-------------INFORMAÇÃO DA CTPS-------------

CTPS: {dados['ctps']}
Ano da contratação: {dados['cont']} Salário: R${dados['sala']:.2f}    
Aposentadoria: {status}     
''')
else:
    print(f'''
------------FICHA DO TRABALHADOR------------

Nome: {dados['nome']}
Ano de Nasc.: {dados['nasc']:<4}             Idade: {dados['idad']}
Nº. CTPS: N/A
''')
print('--------------------------------------------  ')
