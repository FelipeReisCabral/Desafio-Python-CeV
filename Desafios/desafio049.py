# Desafio049: Refaça o DESAFIO 9, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um numero: '))
print('='*12)
print('TABUADA DO {}'.format(n))
print('='*12)
for c in range(1, 11):
    print('{} x {:2} = {:2}' .format(n, c, c*n))
print('='*12)
