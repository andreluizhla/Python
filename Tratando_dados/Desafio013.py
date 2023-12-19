s = float(input('Qual é o salário do funcionário? R$'))

print('O salário que era de \033[mR${:.2f}\033[m, com 15% de aumento,\033[4;32m passa a receber R${:.2f}\033[m'.format(s, s+(s*0.15)))
