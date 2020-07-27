import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no mommento. 🌠💭')
else:
    print('O site está conectado! ⌨💻️')
    print(site.read())



