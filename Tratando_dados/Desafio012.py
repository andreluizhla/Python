from colorama import init
init()
p = float(input('Qual é o preço do produto? R$'))
desconto = 5

print('O produto que custa \033[31mR${:.2f}\033[m, na promoção com \033[1;34mdesconto de {}%\033[m o \033[1;32mproduto custará: R${:.2f}\033[m'.format(p, desconto, p-(p*desconto/100)))
