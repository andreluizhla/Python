dados = list()
pessoas = list()
maiorPeso = menorPeso = 0

while True:
    dados.append(input('Digite o nome: '))
    dados.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else: 
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = input('Deseja continuar? [S/N] ')
    if opcao in 'Nn':
        break
    
print('-=' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorPeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')
print()
