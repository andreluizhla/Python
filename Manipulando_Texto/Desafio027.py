from colorama import init
init()
nome = str(input('Digite o seu nome Completo: '))

nome = nome.split()

print('Primeiro nome: \033[1;32m{}\033[m'.format(nome[0]))
print('Último nome: \033[1;31m{}\033[m'.format(nome[len(nome)-1]))
