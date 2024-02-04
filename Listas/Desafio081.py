valores = list()
cont = 0
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    cont += 1
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
valores.sort(reverse=True)
print(f'Você digitou {cont} números')
print(f'Os em ordem decrescente são: {valores}')
if 5 in valores:
    print('Você digitou o número 5')
else:
    print('Você NÃO digitou o número 5')
