# Desafio107: Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
# também um programa que importe esse módulo e use algumas dessas
# funções.
from funcoes import moeda

preco = float(input('Digite o preço: R$'))
print(f'''A metade de {preco} é {moeda.metade(preco)}
O dobro de {preco} é {moeda.dobro(preco)}
Aumentando 10% de {preco}, temos {moeda.aumentar(preco, 10)}
Reduzindo 13% de {preco}, temos {moeda.reduzir(preco, 13)}''')
