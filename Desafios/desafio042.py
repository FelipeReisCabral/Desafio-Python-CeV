# Desafio042: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
l1 = float(input('Digite o comprimento do 1º lado: '))
l2 = float(input('Digite o comprimento do 2º lado: '))
l3 = float(input('Digite o comprimento do 3º lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l1 == l3:
        print('Com as medidas dos lados {} x {} x {} é possivel formar um triângulo EQUILÁTERO.' .format(l1, l2, l3))
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Com as medidas dos lados {} x {} x {} é possivel formar um triângulo ISÓSCELES.'.format(l1, l2, l3))
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print('Com as medidas dos lados {} x {} x {} é possivel formar um triângulo ESCALENO.'.format(l1, l2, l3))
else:
    print('Com as medidas dos lados {} x {} x {} NÃO é possivel formar um triângulo.' .format(l1, l2, l3))
