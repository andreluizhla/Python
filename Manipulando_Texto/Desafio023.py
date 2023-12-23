from colorama import init
init()
texto = str(input('Digite um número de 0 até 9999: '))

print('Analisando o número \033[4;36m{}\033[m'.format(texto))
print('Unidade: \033[34m{}\033[m'.format(texto[3]))
print('Dezena: \033[34m{}\033[m'.format(texto[2]))
print('Centena: \033[34m{}\033[m'.format(texto[1]))
print('Milhar: \033[34m{}\033[m'.format(texto[0]))
