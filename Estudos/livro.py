minutos = int(input("Minutos usados: "))
if minutos < 200:
    preco = 0.20
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08

print("O valor a ser pago será de R$%6.2f" % (minutos * preco))
