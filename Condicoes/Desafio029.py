vel = float(input('Qual é a velocidade do carro? '))

if vel > 80:
    print('MULTADO')

    multa = (vel - 80) * 7
    print('Você vai pagar {:.2f} reais pela multa'.format(multa))
else:
    print('Está dentro da velocidade')

