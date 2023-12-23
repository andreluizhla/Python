print('===' * 10)
print('{:^30}'.format(' BANCO DOIS IRMÃOS '))
print('===' * 10)
valor = int(input('Que valor você quer sacar? R$'))
quant50 = quant20 = quant10 = 0
while True:
    if valor - 50 >= 0:
        valor -= 50
        quant50 += 1
    elif valor - 20 >= 0:
        valor -= 20
        quant20 += 1
    elif valor - 10 >= 0:
        valor -= 10
        quant10 += 1
    else:
        break
if quant50 != 0:
    print(f'Total de {quant50} cédulas de R$ 50:')
if quant20 != 0:
    print(f'Total de {quant20} cédulas de R$ 20:')
if quant10 != 0:
    print(f'Total de {quant10} cédulas de R$ 10:')
if valor != 0:
    print(f'Total de {valor} cédulas de R$ 1: ')
print('===' * 10)
print('Volte sempre ao BANCO DOIS IRMÃOS! Tenha um bom dia!')
