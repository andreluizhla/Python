from colorama import init
init()
vel = float(input('Qual é a velocidade do carro? '))

if vel > 80:
    print('\033[mVOCÊ FOI MULTADO\033[m')

    multa = (vel - 80) * 7
    print('Você vai pagar \033[4;33m{:.2f} reais pela multa\033[m'.format(multa))

print('\033[4mTenha um bom dia e \033[4;32mdirija com segurança\033[m!')
