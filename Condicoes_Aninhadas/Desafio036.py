casa = float(input('Quanto é a casa? R$ '))
salario = float(input('Quanto é o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))

parcelas = casa / (anos * 12)
minimo = salario * 30 / 100

if minimo >= parcelas:
    print('Pedido de empréstimo \033[1;32mAUTORIZADO!\033[m')
else:
    print('Pedido de empréstimo \033[1;31mNEGADO!\033[m')
