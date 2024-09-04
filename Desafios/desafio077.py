# Desafio077: Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.
palavras = ('cadeira', "mesa", "computador", "caneta", "livro", "telefone",
            "lampada", "quadro", "janela", "porta", "monitor", "teclado",
            "mouse", "mochila", "copo", "garrafa", "prato", "talher", "sofa",
            "televisao")
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()} ', end='')
