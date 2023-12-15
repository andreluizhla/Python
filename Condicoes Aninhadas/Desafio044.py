produto = float(input('Digite o preço do produto: R$'))

print('''Formas de Pagamento: 
1 - À Vista Dinheiro / Cheque
2 - À Vista Cartão
3 - Em até 2x no Cartão
4 - 3x ou mais no Cartão''')

pagamento = int(input('Digite a forma de pagamento: '))

print('O produto custa {:.2f} reais'.format(produto))
print('A forma de pagamento é:')

desconto = 0

preco = produto - (produto * desconto / 100)

if pagamento == 1:
    desconto = 10
    print('À Vista Dinheiro / Cheque e terá {}% de Desconto'.format(desconto))
elif pagamento == 2:
    desconto = 5
    print('À Vista Cartão e terá {}% de Desconto'.format(desconto))
elif pagamento == 3:
    desconto = 0
    print('Em até 2x no Cartão')
    preco = produto
elif pagamento == 4:
    desconto = 120
    print('3x ou mais no Cartão terá 20% de juros')
    preco = produto * desconto / 100

print('Portanto o valor total do produto será de R$ {:.2f}'.format(preco))
