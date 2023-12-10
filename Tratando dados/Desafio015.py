km = float(input('Quantos Km foram rodados? '))
d = int(input('Quantos dias alugados? '))

print('O total a pagar é: R${:.2f}'.format((km * 0.15) + (d * 60)))