from time import sleep


def cores(i):
    """
    ->Sistema básico para adição de cores no sistema
    :param i: valor para adicionar a cor relacionado a lista
    :return: a cor selecionada
    """
    # 0 - Sem cor
    # 1 - Vermelho
    # 2 - Verde
    # 3 - Amarelo
    # 4 - Azul
    # 5 - Roxo
    c = ('\033[m',
         '\033[31m',
         '\033[32m',
         '\033[33m',
         '\033[34m',
         '\033[35m')
    return c[i]


def menuprincipal():
    """
    ->Menu simples para o programa principal
    :return: o Menu principal formatado
    """
    print(f'''{'='*40}
{cores(2)}{'MENU PRINCIPAL':^40}{cores(0)}
{'='*40}
{cores(1)}[1]{cores(0)} - {cores(3)} Ver pessoas cadastradas{cores(0)}
{cores(1)}[2]{cores(0)} - {cores(3)} Cadastrar nova pessoa{cores(0)}
{cores(1)}[3]{cores(0)} - {cores(3)} Sair do sistema{cores(0)}
{'='*40}''')
    sleep(1)


def subtitulo(i):
    """
    -> Cabeçalho de subtitulo para submenus
    :param i: Título do cabeçalho
    :return: Cabeçalho formatado
    """
    print(f'''{'-'*40}
{cores(2)}{i:^40}{cores(0)}
{'_'*40}''')
    sleep(1)


def opcao(n):
    """
    ->Analisa o valor da opção escolhida no menu
    :param n: O valor da opção digitado
    :return: o Valor da opção validado
    """
    while True:
        try:
            op = int(input(n))
            if op == 1:
                subtitulo('LISTA DE PESSOAS')
                lista()
            elif op == 2:
                subtitulo('CADASTRO DE NOVA PESSOA')
                cadastro()
            elif op == 3:
                sleep(1)
                print(f'''
{'-' * 40}
{cores(1)}{f'Saindo do sistema... Até logo!':^40}{cores(0)}
{'-' * 40}''')
                return op
            else:
                print(f'{cores(1)}Erro! Opção inválida{cores(0)}')
                continue
        except (ValueError, TypeError):
            print(f'{cores(1)}Erro! Digite um valor válido do MENU.{cores(0)}')
        except KeyboardInterrupt:
            print(f'{cores(1)}Entrada de opção cancelada pelo usuário.{cores(0)}')
        else:
            return op


def cadastro():
    """
    -> Valida e adiciona Nome e Idade a um arquivo de texto,
     caso arquivo não exista ele cria o arquivo
    :return: Nome e idade cadastrado num arquivo de texto
    """
    while True:
        nome = str(input('Nome: ')).strip().title()
        if not nome:
            print(f'{cores(1)}ERRO! Digite um nome para continuar.{cores(0)}')
            continue
        break
    while True:
        try:
            idade = int(input('Idade: '))
            if idade <= 0:
                print(f'{cores(1)}ERRO! Idade menor ou igual a "0" anos{cores(0)}')
                continue
            break
        except ValueError:
            print(f'{cores(1)}ERRO! Idade não informada{cores(0)}')

    with open('ListaPessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome:<32} {idade:>2} anos\n')
        print(f'{cores(2)}{nome} foi cadastrado com sucesso.{cores(0)}')


def lista():
    """
    -> Verifica se o arquivo de texto existe e exibe o conteudo
    :return: conteudo formatado de um arquivo de texto
    """
    try:
        with open('ListaPessoas.txt', 'r') as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                print(f'''{cores(3)}Arquivo está em branco!!!
Escolha opção {cores(1)}[2]{cores(3)} no MENU
para cadastrar uma pessoa.{cores(0)}''')
            else:
                print(conteudo)
    except FileNotFoundError:
        print(f'''{cores(1)}Arquivo não encontrado!!!{cores(0)}
{cores(3)}Escolha opção {cores(0)}{cores(1)}[2]{cores(0)}{cores(3)} no MENU
para criar o arquivo.{cores(0)}''')
