media = 0
velho = 0
jovensF = 0
nomeVelho = ''
for c in range(1, 5):
    print('-' * 5, end=' ')
    print('{}ª PESSOA'.format(c), end=' ')
    print('-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade
    if idade > velho and sexo == 'M':
        velho = idade
        nomeVelho = nome
    if idade < 20 and sexo == 'F':
        jovensF += 1
media /= 4
print('---' * 10)
print('Com os dados coletados desse grupo temos:')
print('A média de idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos de idade e se chama {}.'.format(velho, nomeVelho))
print('Ao todo têm {} mulheres com menos de 20 anos'.format(jovensF))
