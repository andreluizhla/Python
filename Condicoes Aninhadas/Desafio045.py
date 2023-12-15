from random import choice
from time import sleep

cor = {
    'limpa': '\033[m',
    'ganhou': '\033[1;32m',
    'perdeu': '\033[1;31m',
    'empate': '\033[7;37m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;33m'
}

print('\033[1;32m' + '#' * 30)
print('#   Pedra, Papel e Tesoura   #')
print('#' * 30 + '\033[m')

print('Escolha {}Pedra, Papel ou Tesoura{} e veja se consegue ganhar de mim'.format(cor['amarelo'], cor['limpa']))

escolhas = ['pedra', 'papel', 'tesoura']

jogador = str(input('Digite a sua Escolha: ')).lower().strip()

computador = choice(escolhas)

print('{}PROCESSANDO...{}'.format(cor['azul'], cor['limpa']))
sleep(3)

if jogador in escolhas:

    print('O {}Jogador{} escolheu o(a) {}{}{}'.format('\033[1;33m',  '\033[m', '\033[1;34m', jogador, '\033[m'), end='')
    print(' e o {}Computador{} escolheu o(a) {}{}{}'.format('\033[1;33m', '\033[m', '\033[1;34m', computador, '\033[m'))

    if jogador == computador:
        print('Parece que temos um {}EMPATE{}'.format(cor['empate'], cor['limpa']))
    else:
        if jogador == 'tesoura':
            if computador == 'papel':
                print('{}O Jogador GANHOU{}!'.format(cor['ganhou'], cor['limpa']))
            elif computador == 'pedra':
                print('{}O Computador Ganhou{}'.format(cor['perdeu'], cor['limpa']))
        elif jogador == 'pedra':
            if computador == 'tesoura':
                print('{}O Jogador GANHOU{}!'.format(cor['ganhou'], cor['limpa']))
            elif computador == 'papel':
                print('{}O Computador Ganhou{}'.format(cor['perdeu'], cor['limpa']))
        elif jogador == 'papel':
            if computador == 'pedra':
                print('{}O Jogador GANHOU{}!'.format(cor['ganhou'], cor['limpa']))
            elif computador == 'tesoura':
                print('{}O Computador Ganhou{}'.format(cor['perdeu'], cor['limpa']))
else:
    print('Não consegui identificar se você escolheu Pedra, Papel ou Tesoura')
