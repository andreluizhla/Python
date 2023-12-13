nome = str(input('Digite o seu nome completo: '))

print('Analisando o seu nome...')

print('Seu nome em MAIÚSCULAS fica: \033[4m{}\033[m'.format(nome.upper()))
print('Seu nome em minúsculas fica: \033[4m{}\033[m'.format(nome.lower()))

nome = nome.split()
print('Seu \033[4mnome completo\033[m tem \033[34m{} letras\033[m'.format(len(''.join(nome))))

print('Seu \033[4mprimeiro\033[m nome tem \033[34m{} letras\033[m'.format(len(nome[0])))
