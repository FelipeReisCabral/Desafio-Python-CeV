# Desafio108: Adapte o código do desafio #107, criando uma função
# adicional chamada moeda() que consiga mostrar os números como
# um valor monetário formatado.
from funcoes import moeda

preco = float(input('Digite o preço: R$'))
print(f'''A metade de {moeda.real(preco)} é {moeda.real(moeda.metade(preco))}
O dobro de {moeda.real(preco)} é {moeda.real(moeda.dobro(preco)):}
Aumentando 10% de {moeda.real(preco)}, temos {moeda.real(moeda.aumentar(preco, 10))}
Reduzindo 13% de {moeda.real(preco)}, temos {moeda.real(moeda.reduzir(preco, 13))}''')
