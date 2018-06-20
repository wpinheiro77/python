dias = int(input('Dias de aluguel: '))
km = int(input('Quantidade de kilômetros rodados: '))
pagar = (dias * 60) + (km * 0.15)

print('Você alugou o carro por {} dias e percorreu {}km, valor a ser pago R${:.2f}.' .format(dias, km, pagar))
