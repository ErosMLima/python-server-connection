import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://localhost:8000/')
except urllib.error.URLError:
    print('O site não está acessível no mommento. 🌠💭')
else:
    print('O site está conectado! ⌨💻️')
    print(site.read())
    