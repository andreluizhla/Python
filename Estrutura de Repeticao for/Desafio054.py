from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nascimento = int(input('Em que ano a {}ª nasceu? '.format(pess)))
    idade = atual - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas já são de maior'.format(maior))
print('{} pessoas ainda não são de maior'.format(menor))
