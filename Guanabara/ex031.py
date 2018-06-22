distancia = int(input('Qual a ditância da sua viagem? '))

if distancia <=200:
    print('O preço da passagem será de R${:.2f}' .format(distancia * 0.50))
else:
    print('Opreço da passagem será de R${:.2f}' .format(distancia * 0.45))
