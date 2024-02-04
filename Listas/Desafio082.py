valores = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
