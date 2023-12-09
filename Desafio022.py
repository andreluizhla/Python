nome = str(input('Digite o seu nome completo: '))
print('Analizando o seu nome...')
print(nome.upper())
print(nome.lower())

nome = nome.split()
print('Seu nome completo tem {} letras'.format(len(''.join(nome))))

print('Seu primeiro nome {}, tem {} letras'.format(nome[0], len(nome[0])))