def aumentar(r, aum, f=False):
    valor = (r * aum / 100) + r
    if f:
        return real(valor)
    else:
        return valor


def reduzir(r, red, f=False):
    valor = r - (r * red / 100)
    if f:
        return real(valor)
    else:
        return valor


def dobro(r, f=False):
    valor = r * 2
    if f:
        return real(valor)
    else:
        return valor


def metade(r, f=False):
    valor = r / 2
    if f:
        return real(valor)
    else:
        return valor


def real(r):
    rs = f'R${r:.2f}'.replace('.', ',')
    return rs


def resumo(a, b, c):
    return print(f'''
---------------------------
      RESUMO DO VALOR    
---------------------------
Preço analisado:  {real(a)}
Dobro do preço:   {dobro(a,True)}
Metade do preço:  {metade(a,True)}
{b}% de aumento:   {aumentar(a, b, True)}
{c}% de redução:   {reduzir(a, c, True)}
---------------------------''')
