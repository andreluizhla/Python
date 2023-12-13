km = float(input('Quantos Km foram rodados? '))
d = int(input('Quantos dias alugados? '))

print('O total a pagar é: \033[4;33mR${:.2f}\033[m'.format((km * 0.15) + (d * 60)))