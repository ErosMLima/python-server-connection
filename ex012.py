preço = float(input("Qual é o preço do produto? R$ "))
novo = preço - (preço * 30 / 100)
print('O produto que custava  R${:.2f},\n na promoção com desconto de 30%\n vai custar R${:.2f}'.format(preço, novo))
