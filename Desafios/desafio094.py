# Desafio094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
lista = list()
pessoa = dict()
media = 0
while True:
    print('''_______________BANCO DE PESSOAS_______________
    [1] - Cadastrar nova pessoa.
    [2] - Total de pessoas no grupo.
    [3] - Média de idade do grupo.
    [4] - Mulheres do grupo.
    [5] - Pessoas com idade acima da média.
    [0] - Sair. ''')
    print('==============================================')
    op = int(input('Opção desejada: '))
    if op == 1:
        print('_______________TELA DE CADASTRO_______________')
        pessoa["nome"] = str(input('Nome: ')).strip().title()
        pessoa["sexo"] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa["sexo"] not in 'MF':
            pessoa["sexo"] = str(input('Entrada inválida, digite novamente! [M/F]: ')).strip().upper()
        pessoa["idade"] = int(input('Idade: '))
        lista.append(pessoa.copy())
        pessoa.clear()
    if op == 2:
        print(f'''________________TOTAL DO GRUPO________________
        
Total de pessoas cadastradas: {len(lista)}
''')
    if op == 3:
        for i in range(0, len(lista)):
            media += lista[i]["idade"]

        print(f'''________________MÉDIA DE IDADE________________
        
Soma da  idade do grupo: {media} anos
Total de cadastradas: {len(lista)} pessoas
Média de idade do grupo: {media / len(lista):.2f}
''')
    if op == 4:
        print('''______________LISTA DAS MULHERES______________
''')
        for i in range(0, len(lista)):
            if lista[i]['sexo'] in "F":
                print(f'-- {lista[i]["nome"]}')
    if op == 5:
        for i in range(0, len(lista)):
            media += lista[i]["idade"]
        media = media / len(lista)
        print(f'__________PESSOAS ACIMA DE {media:.1f} ANOS__________')
        for i in range(0, len(lista)):
            if lista[i]["idade"] >= media:
                print(f'''    Nome: {lista[i]["nome"]}
    Sexo: {'Feminino' if lista[i]["sexo"] == 'F' else 'Masculino'}
    Idade {lista[i]["idade"]} anos
______________________________________________''')
    if op == 0:
        print('ENCERRANDO CADASTROS...')
        break
