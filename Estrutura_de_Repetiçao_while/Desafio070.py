total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    if cont == 1 or preco < menor:    
        if menor > preco:
            menor = preco
            barato = produto
        if preco >= 1000:
            totmil += 1
        total += preco
    else: 
        total = menor = preco
        barato = produto
    opcao = ''
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra foi R${total}')
print(f'Tem {totmil} produtos que custam mais de R$1000,00')
print(f'O produto mais barato é {barato}custando R${menor}')
