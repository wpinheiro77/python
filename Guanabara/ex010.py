reais = float(input('Digite quanto dinheiro você tem: '))
dolar = 3.27
compra = reais / dolar

print('Com R${} você pode comprar US${:.2f}' .format(reais, compra))
