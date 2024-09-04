# Desafio105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
def notas(* n, sit=False):
    """
    -> Analisa notas e situações de uma lista de notas
    :param n: Recebe uma ou mais notas
    :param sit: (opcional) False = Não exibe a situação, True = exibe a situação
    :return: Dicionario com várias informações sobre a situação da turma
    """
    lista = dict()
    lista["total"] = len(n)
    lista["maior"] = max(n)
    lista["menor"] = min(n)
    lista["media"] = sum(n) / len(n)
    if sit:
        if lista["media"] >= 7:
            lista["situação"] = 'BOA'
        elif lista["media"] < 5:
            lista["situação"] = 'RUIM'
        else:
            lista["situação"] = 'RAZOÁVEL'
    return lista

#Notas passadas dentro dos parentes junto com a situação (True ou False)
x = notas(5.5, 2.5, 1.5, sit=True)
print(x)
