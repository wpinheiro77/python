preco = float(input('Digite o valor do produto: '))
novo = preco - (preco * 0.05)

print('O preco do produto à vista com 5% de desconta será de R${0:.2f}' .format(novo))
