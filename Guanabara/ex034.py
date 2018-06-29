salario = int(input('Digite o salário: '))

if salario > 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario *0.15)

print('O novo salário será de R${:.2f}' .format(salario))
