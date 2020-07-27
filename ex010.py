#Exercicio 10 crie um programa que leia quanto dinheiro uma pessoa tem na
#carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('O valor em carteira: '))
dolar = 1
reais = 3.27
wallet = carteira * (reais * dolar)
print("O valor de ${} dólares vale ${} totalizando um montante de ${} dólares na sua carteira".format(reais, dolar, carteira))
