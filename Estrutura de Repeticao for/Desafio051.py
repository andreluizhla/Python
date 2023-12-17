termo = int(input('Digite o primeiro termo: '))
r = int(input('Digita a razão: '))
print('Os 10 primeiros termos da PA é: (', end='')
for c in range(1, 10):
    print(termo, end=', ')
    termo += r
print(termo, end=')')
