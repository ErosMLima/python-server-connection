#Exercicio 17
#Comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo

#maneira 1
'''co = float(input('cateto oposto: '))
ca = float(input('cateto adjascente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

from math import hypot
co = float(input('cateto oposto: '))
ca = float(input('cateto adjascente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir  {:.2f}'.format(hi))