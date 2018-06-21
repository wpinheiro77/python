import math
catetoOp = int(input('Digite o cateto oposto: '))
catetoAd = int(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(catetoOp, catetoAd)

print('A hipotenusa dos catetos {} e {} é {:.2f}.' .format(catetoOp, catetoAd, hipotenusa))
