#tres ganhadores vão recber 780 mil
#primeiro receberá 46%
#segundo receberá 32%
#terceiro receberá o restante

premio = int(780000)

primeiro = premio - (premio * 0.54)
segundo = premio + (premio * 0.68)
terceiro = premio - (segundo + primeiro)

print('Primeiro premio = R${0:.2f}' .format(primeiro))
print('segundo premio = R${0:.2f}' .format(segundo))
print('Primeiro premio = R${0:.2f}' .format(terceiro))
