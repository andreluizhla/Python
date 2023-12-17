media = 0
velho = 0
jovensF = 0
nomeVelho = ''
for c in range(1, 5):
    print('-==-' * 10)
    print('Pessoa {}'.format(c))
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo (M ou F): ')).upper()
    media += idade
    if idade > velho and sexo == 'M':
        velho = idade
        nomeVelho = nome

    if idade < 20 and sexo == 'F':
        jovensF += 1

media /= 4
print('-==-' * 10)
print('Com os dados coletados desse grupo temos:')
print('A média de idade é {}'.format(media))
print('O {} é o mais velho do grupo com {} anos de idade'.format(nomeVelho, velho))
print('Têm {} mulheres com menos de 20 anos de idade'.format(jovensF))
