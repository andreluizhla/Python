dados = list()
pessoas = list()
maiorPeso = 0
menorPeso = 100
maiorPessoa = []
menorPessoa = []
c = 0
while True:
    dados.append(input('Digite o nome: '))
    dados.append(float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    if pessoas[c][1] > maiorPeso:
        maiorPeso = pessoas[c][1]
    if pessoas[c][1] < menorPeso:
        menorPeso = pessoas[c][1]
    opcao = input('Deseja continuar? [S/N] ')
    if opcao in 'Nn':
        break
    c += 1
for c in range(0, len(pessoas)):
    if pessoas[c][1] == maiorPeso:
        maiorPessoa.append(pessoas[c][0])
    if pessoas[c][1] == menorPeso:
        menorPessoa.append(pessoas[c][0])
    
print('-=' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de {maiorPessoa}')
print(f'O menor peso foi de {menorPeso}Kg. Peso de {menorPessoa}')
