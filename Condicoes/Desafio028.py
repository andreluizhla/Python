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
    print('\033[1;33mPARABÉNS!\033[m \033[4;32mVocê ganhou!\033[m')
else: 
    print('Que Pena. \033[1;31mVocê Perdeu\033[m')
    print('O número que eu pensei foi: \033[1;35m{}\033[m'.format(numPens))
