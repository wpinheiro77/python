from random import randint
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))
if jogador == computador:
    print('Parabens! Você acertou, eu pensei no número {}!' .format(computador))
else:
    print('Ganhei! Eu pensei no número {} e não no número {}' .format(computador, jogador))

