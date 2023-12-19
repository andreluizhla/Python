sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Por favor digite de novo: ')).strip().upper()[0]
print('Tudo certo')
