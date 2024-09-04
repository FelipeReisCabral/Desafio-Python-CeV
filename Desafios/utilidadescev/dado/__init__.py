def leiaDinheiro(valor=''):
    while True:
        teste = input(valor).replace(',', '.').strip()
        if teste.replace('.', '').isdigit():
            return float(teste)
        else:
            print(f'\033[0;31mERRO! \"{teste}\" não é um valor numérico.\033[m')
