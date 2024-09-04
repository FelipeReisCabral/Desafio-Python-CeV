# Desafio041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
cat = date.today().year - ano
if cat <= 9:
    x = 'MIRIM'
elif cat <= 14:
    x = 'INFANTIL'
elif cat <= 19:
    x = 'JUNIOR'
elif cat <= 25:
    x = 'SÊNIOR'
else:
    x = 'MASTER'
print('Idade: {}\nCategoria: {}' .format(cat, x))
