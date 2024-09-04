# Desafio106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário
# digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
def titulo(msg):
    """
    ->Cria um cabeçalho alinhado com cores
    :param msg: O titulo do cabeçalho
    :return: Cabeçalho formatado
    """
    x = len(msg) + 4
    print('\033[30;44;1m~' * x)
    print(f'  {msg}')
    print('~' * x)
    print('\033[m')


def comando(cmd):
    """
    ->Pesquisa no manual interno do python a função do comando pedido
    :param cmd: comando a ser pesquisado
    :return: o manual do comando solicitado
    """
    barra = 34 + len(cmd)
    print('\033[30;46;1m~' * barra)
    print(f'  Acessando Manual do Comando "{cmd}"')
    print('~' * barra)
    print('\033[47m')
    help(cmd)


while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    ajuda = str(input('Função ou Biblioteca ("fim" para sair)>>> ')).strip()
    if ajuda.lower() == 'fim':
        print('Fechando o Sistema de ajuda')
        break
    else:
        comando(ajuda)
