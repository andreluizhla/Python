from random import randint
from time import sleep

numPens = randint(0, 5)

print('--=' * 20)
print('Pensei em um número entre 0 e 5. Tente adivinhar...')
print('--=' * 20)

tent = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(5)

if tent == numPens:
    print('PARABÉNS! Você ganhou!')
else: 
    print('Que Pena. Você Perdeu')
    print('O número que eu pensei foi: {}'.format(numPens))
