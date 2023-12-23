from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
vitorias = 0
while True:
    print('#' * 25)
    num = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = num + computador
    tipo = ''
    while tipo not in 'PÍI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 25)
    print(f'Você jogou {num} e o computador {computador}. Total de {soma}', end=' ')
    if soma % 2 == 0:
        res = 'P'
        print('DEU PAR.')
    else:
        res = 'ÍI'
        print('DEU ÍMPAR.')
    if tipo in res:
        print('Você GANHOU!')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
print('==' * 25)
print(f'GAME OVER! Você venceu {vitorias} vezes.')
