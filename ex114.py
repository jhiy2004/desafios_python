import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except Exception:
    print('Falha ao abrir o site Pudim')
else:
    print('Sucesso ao abrir o site')
    print(site.read())