from math import hypot
co = int(input('Comprimento do cateto oposto: '))
ca = int(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa é igual a \033[1;34m{:.2f}\033[m'.format(hi))
