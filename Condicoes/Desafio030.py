from colorama import init
init()
num = int(input('Digite um número: '))

if num % 2 == 0:
    print('O número {} é \033[1;32mPAR\033[m!'.format(num))
else:
    print('O número {} é \033[1;31mÍMPAR\033[m!'.format(num))
