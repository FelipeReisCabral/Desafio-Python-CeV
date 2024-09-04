def aumentar(r=0, aum=0, f=False):
    valor = (r * aum / 100) + r
    if f:
        return real(valor)
    else:
        return valor


def reduzir(r=0, red=0, f=False):
    valor = r - (r * red / 100)
    if f:
        return real(valor)
    else:
        return valor


def dobro(r=0, f=False):
    valor = r * 2
    if f:
        return real(valor)
    else:
        return valor


def metade(r=0, f=False):
    valor = r / 2
    if f:
        return real(valor)
    else:
        return valor


def real(r=0):
    rs = f'R${r:.2f}'.replace('.', ',')
    return rs


def resumo(a=0, b=0, c=0):
    return print(f'''
{'-'*35}
{'RESUMO DO VALOR':^35}
{'-'*35}
Preço analisado:\t\t{real(a)}
Dobro do preço:\t\t\t{dobro(a,True)}
Metade do preço:\t\t{metade(a,True)}
{b}% de aumento:\t\t\t{aumentar(a, b, True)}
{c}% de redução:\t\t\t{reduzir(a, c, True)}
{'-'*35}''')
