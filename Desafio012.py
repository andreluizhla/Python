p = float(input('Qual é o preço do produto? R$'))
desconto = 5

print('O produto que custa R${:.2f}, na promoção com desconto de {}% o produto custará: R${:.2f}'.format(p, desconto, p-(p*desconto/100)))