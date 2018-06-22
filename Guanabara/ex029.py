velocidade = int(input('Velocidade do automóvel: '))
multa = (velocidade - 80) *7

if velocidade <= 80:
    print("Boa viagem!")
else:
    print('Você excedeu o limite de velocidade, a multa a ser paga será de R${:.2f}' .format(multa))
