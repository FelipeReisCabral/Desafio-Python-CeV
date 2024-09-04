# Desafio095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
lista = list()
jogador = dict()
gol = list()
total = 0
while True:
    print('''________ESTATÍSTICAS DE JOGADORES________
    [1] - Cadastra novo jogador.
    [2] - Ir para está estatísticas''')
    op = int(input('Opção desejada: '))
    if op == 1:
        jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
        part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        for i in range(0, part):
            gol.append(int(input(f'Quantos gols {jogador["nome"]} marcou no {i+1}º jogo? ')))
        jogador["gols"] = gol
        for i in range(0, len(gol)):
            total += gol[i]
        jogador["gols"] = gol[:]
        jogador["total"] = total
        jogador["media"] = jogador["total"] / part
        lista.append(jogador.copy())
        jogador.clear()
        gol.clear()
        total = 0
    if op == 2:
        break
while op != 999:
    print('____LISTA DE JOGADORES____')
    print(f'{'No.':<7}{'NOME':<9}{'TOTAL DE GOLS'}')
    for k, v in enumerate(lista):
        print(f'{k:<3} - {v['nome']:<15}{v["total"]:>2}')
    print('999 - Sair')
    op = int(input('Informe No. do Jogador para ver gols: '))
    if op != 999:
        totalgols = 0
        print(f'____GOLS DE {lista[op]['nome'].upper()}____')
        for i in range(0, len(lista[op]['gols'])):
            print(f'{i+1}º jogo: {lista[op]['gols'][i]} gols')
            totalgols += lista[op]['gols'][i]
        print(f'''Total de gols de {lista[op]['nome']}: {totalgols} gols
Média de {lista[op]['nome']}: {lista[op]['media']:.1f} gols p/ partida''')
        print('='*20)
print('SAINDO')
