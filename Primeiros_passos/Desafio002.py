from colorama import init
init()
nome = input('Qual é o seu nome? ')
print('Seja muito bem vindo \033[4;32m{}\033[m!'.format(nome))
