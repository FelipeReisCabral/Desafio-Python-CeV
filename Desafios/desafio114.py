# Desafio114: Crie um código em Python que teste se o site do Google está
# acessível pelo computador usado.
import urllib
import urllib.request
try:
    urllib.request.urlopen('https://www.google.com/')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Sucesso')
