from colorama import init
init()
# Código feito em maio de 2023, e o dólar estava R$5,00

dinheiro = float(input('Quanto Reais você tem? R$'))

print('Com \033[4;32m{:.2f} reais\033[m, você pode comprar \033[1;31m{:.2f} dólares\033[m'.format(dinheiro, dinheiro / 5))
