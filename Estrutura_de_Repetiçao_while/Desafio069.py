maioridade = homens = jovensF = 0
while True:
    sexo = opcao = ''
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        jovensF += 1
    print('-' * 25)
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('=========FIM DO PROGRAMA=========')
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {jovensF} mulheres com menos de 20 anos')
