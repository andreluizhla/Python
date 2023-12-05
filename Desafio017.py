from math import hypot
co = int(input('Comprimento do cateto oposto: '))
ca = int(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipoternusa é igual a {:.2f}'.format(hi))
