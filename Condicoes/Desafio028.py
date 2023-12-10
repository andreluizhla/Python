from random import randint

numPens = randint(0, 5)
print('Pensei em um número entre 0 e 5, vamos ver se você consegue adivinhar.')

tent = int(input('Qual é o seu chute? '))

if tent == numPens:
    print('O usuário ganhou!')
else: 
    print('O Computador ganhou!')
    print('O número escolhido foi: {}'.format(numPens))