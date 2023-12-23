from math import pi
from colorama import init
init()

num = int(input('Digite o raio da circunferência: '))
c = 2 * pi * num
print('A circunferência desse círculo é igual a {:.2f}'.format(c))