# Desafio083: Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.
exp = str(input('Digite uma expressão:'))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Expressão correta.')
else:
    print('Expressão incorreta.')
    