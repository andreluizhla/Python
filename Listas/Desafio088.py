from random import randint
from time import sleep
lista = []

print('-' * 30)
print(f'{'Jogos na Mega Sena': ^30}')
print('-' * 30)
sorteie = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{'-=' * 3} SORTEANDO {sorteie} JOGOS {'-=' * 3}')
for n in range(1, sorteie + 1):
    while len(lista) < 6:
        num_aleat = randint(1, 60)
        if num_aleat not in lista:
            lista.append(num_aleat)
    lista.sort()
    print(f'Jogo {n}: {lista}')
    lista.clear()
    sleep(1)
print(f'{'-=' * 5} < BOA SORTE! > {'-=' * 5}')
