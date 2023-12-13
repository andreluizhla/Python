from math import trunc
n = float(input('Digite um número: '))
print('O número \033[1;34m{}\033[m tem a parte inteira \033[4;32m{}\033[m'.format(n, trunc(n)))
