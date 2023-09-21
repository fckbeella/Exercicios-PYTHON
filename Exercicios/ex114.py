import urllib
import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br')
except:
    print('O site PUDIM nao esta acessivel no momento.')
else:
    print('Consegui acessar o site PUDIM com sucesso!')


import webbrowser
try:
    webbrowser.open('http://pudim.com.br')
except:
    print('O site PUDIM nao esta acessivel no momento.')
else:
    print('Consegui acessar o site PUDIM com sucesso!')