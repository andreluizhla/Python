from random import randint
lista = []

print('-' * 31)
print('Jogos na Mega Sena')
print('-' * 31)
sorteie = int(input('Quantos jogos você quer que eu sorteie? '))
for n in range(0, sorteie):
    while len(lista) < 6:
        num_aleat = randint(1, 60)
        if num_aleat not in lista:
            lista.append(num_aleat)
    lista.sort()
    print(f'Jogo {n}: {lista}')
    lista.clear()