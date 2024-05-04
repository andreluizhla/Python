#numeros = [[pares], [impares]]
numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
        numeros[0].sort()
    else:
        numeros[1].append(n)
        numeros[1].sort()
print('-=-' * 15)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
