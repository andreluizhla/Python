from colorama import init
init()
salario = float(input('Qual é o salário do funcionário? R$'))

if salario >= 1250:
    aumento = (salario * 10 / 100) + salario
else:
    aumento = (salario * 15 / 100) + salario
print('Quem ganhava \033[1;33mR${:.2f}\033[m passa a ganhar \033[4;32mR${:.2f}\033[m'.format(salario, aumento))
