y = int(input("Digite um número inteiro maior que zero: "))
x = 1
if x <= 0:
    print('Valor inválido, por favor digite um valor inteiro maior que zero!')
while x <= y:
    print(x)
    x = x + 2