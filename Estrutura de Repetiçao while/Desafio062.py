print('-' * 8, 'PROGRESSÃO ARITMÉTICA', '-' * 8)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
termo = primeiro + razao
print('Os 10 primeiros termos da PA são: {}'.format(primeiro), end=', ')
while termo <= decimo:
    print(termo, end=', ')
    termo += razao
print('FIM.')
enezimaPosicao = int(input('Digite até que termo deseja saber, digite 0 para cancelar: '))
while enezimaPosicao != 0:
    if enezimaPosicao != 0:
        print('\nOs próximos {} termos da PA são:'.format(enezimaPosicao, termo), end=' ')
        enezimoTermo = termo + (enezimaPosicao - 1) * razao
        while termo <= enezimoTermo:
            print(termo, end=', ')
            termo += razao
        print('FIM.')
        enezimaPosicao = int(input('Digite até que termo deseja saber, digite 0 para cancelar: '))
print('Obrigado por usar o programa!')
