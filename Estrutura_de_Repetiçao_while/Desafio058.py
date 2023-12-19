from random import randint
computador = randint(1, 10)
print('=' * 20)
print('Jogo da Adivinhação')
print('=' * 20)
print('Pensei em um número entre 1 e 10, vamos ver se consegue adivinhar')
tentativas = 0
acertou = False

while not acertou:
    jogador = int(input('Chute: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\nÉ Maior... Tente Novamente.')
        elif jogador > computador:
            print('\nÉ Menor... Tente Novamente.')
print('Você acertou, o número que eu pensei foi: {}'.format(computador))
print('Você precisou de {} tentativas para acertar'.format(tentativas))
