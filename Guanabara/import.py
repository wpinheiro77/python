import math
# from math import sqrt   - Assim voê importa somente o SQRT da biblioteca MATH
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('a raiz de {} é {}' .format(num, math.ceil(raiz)))
