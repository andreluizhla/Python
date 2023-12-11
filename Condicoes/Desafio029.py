vel = float(input('Qual é a velocidade do carro? '))

if vel > 80:
    print('VOCÊ FOI MULTADO')

    multa = (vel - 80) * 7
    print('Você vai pagar {:.2f} reais pela multa'.format(multa))

print('Tenha um bom dia e dirigja com segurança!')
