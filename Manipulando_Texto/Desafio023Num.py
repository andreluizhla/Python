from colorama import init
init()
num = int(input('Digite um número de 0 até 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número \033[4;36m{}\033[m'.format(num))
print('Unidade: \033[34m{}\033[m'.format(u))
print('Dezena: \033[34m{}\033[m'.format(d))
print('Centena: \033[34m{}\033[m'.format(c))
print('Milhar: \033[34m{}\033[m'.format(m))
