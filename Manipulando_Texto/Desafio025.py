from colorama import init
init()
nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome têm Silva? \033[4;34m{}\033[m'.format('silva' in nome.lower()))