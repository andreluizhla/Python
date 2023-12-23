from random import choice
from time import sleep
from colorama import init
init()
cor = {
    'limpa': '\033[m',
    'ganhou': '\033[1;32m',
    'perdeu': '\033[1;31m',
    'empate': '\033[4;33m',
    'azul': '\033[1;34m',
    'amar': '\033[1;33m',
    'verde': '\033[1;32m'
}
print(cor['verde'] + '#' * 30)
print('#   Pedra, Papel e Tesoura   #')
print('#' * 30 + cor['limpa'])

print('Faça a sua {}escolha{} e veja se consegue ganhar de mim'.format(cor['amar'], cor['limpa']))
print('''{}[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA{}'''.format(cor['azul'], cor['limpa']))
opcao = int(input('Escolha sabiamente a sua jogada: '))
if opcao != 1 and opcao != 2 and opcao != 3:
    print('{}OPÇÃO INVÁLIDA. TENTE NOVAMENTE{}'.format(cor['perdeu'], cor['limpa']))
else:
    if opcao == 1:
        jogador = 'Pedra'
    elif opcao == 2:
        jogador = 'Papel'
    else:
        jogador = 'Tesoura'
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    computador = choice(escolhas)
    print('{}JO{}'.format(cor['verde'], cor['limpa']))
    sleep(1)
    print('{}KEN{}'.format(cor['verde'], cor['limpa']))
    sleep(1)
    print('{}PO{}!'.format(cor['verde'], cor['limpa']))
    sleep(0.5)
    print('-=-' * 15)
    print(f'{cor['amar']}Jogador{cor['limpa']} jogou {cor['azul']}{jogador}{cor['limpa']}')
    print(f'{cor['amar']}Computador{cor['limpa']} jogou {cor['azul']}{computador}{cor['limpa']}')
    print('-=-' * 15)
    if jogador == computador:
        print('Parece que temos um {}EMPATE{}'.format(cor['empate'], cor['limpa']))
    else:
        if jogador == 'Tesoura':
            if computador == 'Papel':
                print('{}O Jogador GANHOU{}!'.format(cor['ganhou'], cor['limpa']))
            elif computador == 'Pedra':
                print('{}O Computador Ganhou{}'.format(cor['perdeu'], cor['limpa']))
        elif jogador == 'Pedra':
            if computador == 'Tesoura':
                print('{}O Jogador GANHOU{}!'.format(cor['ganhou'], cor['limpa']))
            elif computador == 'Papel':
                print('{}O Computador Ganhou{}'.format(cor['perdeu'], cor['limpa']))
        elif jogador == 'Papel':
            if computador == 'Pedra':
                print('{}O Jogador GANHOU{}!'.format(cor['ganhou'], cor['limpa']))
            elif computador == 'Tesoura':
                print('{}O Computador Ganhou{}'.format(cor['perdeu'], cor['limpa']))
