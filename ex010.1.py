#Exercicio 10 crie um programa que leia quanto dinheiro uma pessoa tem na
#carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem na sua carteira? R$'))
dolar = real / 5
reais = 5
print("Com R${:.2f} você pode comprar US${:.2f}".format(reais, dolar))
