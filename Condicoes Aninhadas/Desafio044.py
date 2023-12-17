preco = float(input('Digite o preço das compras: R$'))

print('''Formas de Pagamento: 
[ 1 ] À Vista Dinheiro / Cheque
[ 2 ] À Vista Cartão
[ 3 ] Em até 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')

opcao = int(input('Qual é a sua opção? '))
total = preco
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    parcelas = preco / 2
    print('Sua compra será parcelada em 2x pagando R${:.2f} SEM JUROS'.format(parcelas))
elif opcao == 4:
    total = (preco * 20 / 100) + preco
    parcelas = int(input('Quantas parcelas? '))
    totparcelado = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, totparcelado))
else:
    print('\033[4;31mOPÇÃO INVÁLIDA de pagamento. Tente Novamente\033[m')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
