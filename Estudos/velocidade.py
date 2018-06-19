vel = int(input("Qual é a velocidade do carro? "))

if vel > 110:
    print("Você foi multado!")
    multa = (vel -110) *5
    print("valor da multa: R$ %5.2f" % multa)
if vel == 110:
    print("Cuidado, você está no limite da velocidade máxima permitida!")
if vel < 110:
    print("Prossiga a sua viagem!")
