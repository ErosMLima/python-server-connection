from random import shuffle

n1 = str(input('Primeiro número do bingo: '))
n2 = str(input('Segundo número do bingo: '))
n3 = str(input('Terceiro número do bingo: '))
n4 = str(input('Quarto número do bingo: '))
n5 = str(input('Quinto número do bingo: '))
n6 = str(input('Sexto número do bingo: '))
n7 = str(input('Sétimo número do bingo: '))
n8 = str(input('Oitavo número do bingo: '))

lista = [n1, n2, n3, n4, n5, n6, n7, n8 ]
shuffle(lista)
print('Os números sorteados foram: ')
print(lista)
