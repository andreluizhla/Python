valores = list()
while True:
    num = int(input('Digite um número: '))
    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Número adicionado com sucesso...')
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os seguintes valores: {valores}')
