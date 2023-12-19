print('-' * 5, 'PROGRESSÃO ARITMÉTICA', '-' * 5)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
print('Os 10 primeiros termos da PA são: {}'.format(primeiro), end=', ')
termo = primeiro + razao
while termo <= decimo:
    print(termo, end=', ')
    termo += razao
print('Fim')
