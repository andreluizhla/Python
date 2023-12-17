from datetime import date
ano = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input('digite o seu ano de nascimento: '))
    if ano - nascimento >= 18:
        maior += 1
    else:
        menor += 1

print('{} pessoas já são de maior'.format(maior))
print('{} pessoas ainda não são de maior'.format(menor))
