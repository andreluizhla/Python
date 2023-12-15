print('IMC (Índice de Massa Corporal)')

altura = float(input('Digite a sua altura em Metros: '))
peso = float(input('Digite o seu peso: Kg '))

imc = peso / altura ** 2
print('Seu IMC é de {:.1f}'.format(imc))
print('Então você têm: ')

if imc <= 18.5:
    print('ABAIXO DO PESO')
elif 18.5 < imc <= 25:
    print('PESO IDEAL')
elif 25 < imc <= 30:
    print('SOBREPESO')
elif 30 < imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
