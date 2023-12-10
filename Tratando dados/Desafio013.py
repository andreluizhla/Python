s = float(input('Qual é o salário do funcionário? R$'))

print('O salário que era de R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, s+(s*0.15)))