# Desafio093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.
aprov = dict()
gol = list()
total = 0

print('________CADASTRO DO JOGADOR________')
aprov['nome'] = str(input('Nome do Jogador: ')).strip().title()
part = int(input(f'Quantas partida {aprov["nome"]} jogou? '))
for i in range(0, part):
    gol.append(int(input(f'Quantos gols {aprov["nome"]} marcou no {i+1}º jogo? ')))
aprov["gols"] = gol[:]
for i in range(0, len(gol)):
    total += gol[i]
aprov["total"] = total
media = total/part
print(f'''
--ESTASTISTICAS DE {aprov["nome"].upper()}--
Partidas Jogadas: {part} jogos.
------------------''')
for i, v in enumerate(gol):
    print(f'{i+1}º jogo: {v} gols')
print(f'''------------------
Total de gols: {total}
Média: {media:.1f} gols p/ partida.
----------------------------------
''')
