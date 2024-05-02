valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break
for pos, val in enumerate(valores):
    if val % 2 == 0:
        pares.append(val)
    else:
        impares.append(val)
    
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
