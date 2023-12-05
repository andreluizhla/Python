p = float(input('Qual é o preço do produto? R$'))

print('O produto que custa R${:.2f}, na promoção com desconto de 5% o produto custará: R${:.2f}'.format(p, p-(p*0.05)))