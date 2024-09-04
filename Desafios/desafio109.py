# Desafio109: Modifique as funções que form criadas no desafio 107 para que
# elas aceitem um parâmetro a mais, informando se o valor retornado por
# elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from funcoes import moeda

preco = float(input('Digite o preço: R$'))
print(f'''A metade de {moeda.real(preco)} é {moeda.metade(preco, True)}
O dobro de {moeda.real(preco)} é {moeda.dobro(preco, True):}
Aumentando 10% de {moeda.real(preco)}, temos {moeda.aumentar(preco, 10, True)}
Reduzindo 13% de {moeda.real(preco)}, temos {moeda.reduzir(preco, 13, True)}''')
