#Receber a altura do degrau de uma escada e a altura que o usuario deseja alcançar
#Calcular quantos degraus o usuário deve subir para atingir a meta

degrau = float(input('Digite a altura dos degraus: '))
altura = float(input('Digite a altera que deseja alcançar: '))

qtdDegraus = int(altura / degrau)

print('Você terá que subir {} degraus para subir {} metros!' .format(qtdDegraus, altura))
