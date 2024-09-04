# Desafio062: Melhore o DESAFIO 61, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerrará quando ele disser que
# quer mostrar 0 termos.
termo = int(input('Informe o primeiro termo da PA:'))
razao = int(input('Informe a razão da PA: '))
opcao = 10
while opcao != 0:
    c = 0
    while c < opcao:
        print('{}'.format(termo), end='-')
        termo = termo + razao
        c += 1
    opcao = int(input('PAUSA\nQuantos termos deseja ver mais: '))
print('SAINDO...')
