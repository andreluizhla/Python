primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digita a razão: '))
decimo = primeiro + (10 - 1) * razao
print('Os 10 primeiros termos da PA é: (', end='')
for termo in range(primeiro, decimo + razao, razao):
    print(termo, end=', ')
print(end=')')
