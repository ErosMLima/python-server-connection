salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('um funcionário que ganhava R${:.2f},\n com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
