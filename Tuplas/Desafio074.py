from random import randint
aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores gerados foram: ', end='')
for val in aleatorios:
    print(val, end=' ')
print(f'\nO menor número da lista foi o {min(aleatorios)}')
print(f'O maior número da lista foi o {max(aleatorios)}')
