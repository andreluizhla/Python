from datetime import date

nascimento = int(input('Digite o ano que você nasceu: '))
ano = date.today().year
idade = ano - nascimento

if idade < 18:
    print('Você ainda vai se alistar no exercito')
elif idade == 18:
    print('Está na hora de se alistar para o exercito')
else:
    print('Já passou do tempo de alistamento')
