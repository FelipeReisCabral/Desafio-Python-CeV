# Desafio087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
i = somapar = somacoluna = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
       matriz[l][c] = (int(input(f'Digite um valor para [{l}, {c}]')))
print('='*21)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]
    somacoluna += matriz[l][2]

    print()
print(f'''{'='*21}
A) A Soma de todos os valores pares é: {somapar}'
B) A soma dos valores da terceira coluna é: {somacoluna}
C) O Maior valor da segunda linha foi: {maior}''')
