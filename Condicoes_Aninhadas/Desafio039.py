from colorama import init
from datetime import date
init()
nascimento = int(input('Digite o ano que você nasceu: '))
ano = date.today().year
idade = ano - nascimento

print('Quem nasceu em {} tem {} em {}'.format(nascimento, idade, ano))

if idade < 18:
    print('Ainda falta {} anos para seu alistamento'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(nascimento + 18))
elif idade == 18:
    print('Está na hora de se alistar para o exercito')
else:
    print('Você deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(nascimento + 18))
