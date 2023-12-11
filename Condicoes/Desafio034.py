salario = float(input('Qual é o seu salário? R$'))

print('Seu novo salário será de: ')
if salario > 1200:
    print('{} reais'.format(salario * 0.1 + salario))
else:
    print('{} reais'.format(salario * 0.15 + salario))