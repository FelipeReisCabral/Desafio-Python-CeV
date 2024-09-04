def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31;1mErro: A entrada não é um número inteiro válido. Tente novamente.\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\n\033[31;1mO usuário finalizou a execução!\033[m")
            return 0
        else:
            return inteiro


def leiaReal(msg):
    while True:
        try:
            real = float(input(msg))
        except ValueError:
            print('\033[31;1mErro: A entrada não é um número real válido. Tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31;1mO usuário finalizou a execução!\033[m')
            return 0
        else:
            return real
