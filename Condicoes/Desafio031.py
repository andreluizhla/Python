viagem = float(input('Digite a distância da viagem em Km: '))

print('Você vai pagar:')
if viagem < 200:
    print('{} reais'.format(viagem * 0.5))
else:
    print('{} reais'.format(viagem * 0.45))

print('Tenha uma boa viagem!')
