from colorama import init
init()
n = int(input('Escreva um número: '))

print('O dobro do número \033[31m{}\033[m, é: \033[34m{}\033[m, o triplo desse número é: \033[32m{}\033[m, e a raiz quadrada desse número é: \033[33m{}\033[m'.format(n, n*2, n*3, n**(1/2)))