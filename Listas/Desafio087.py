tabela = [[], [], []]
soma_total = soma_terceira = maior_segunda = 0

for lin in range(0, 3):
    for col in range(0, 3):
        numero = int(input(f'Digite um valor para [{lin}, {col}]: '))
        tabela[lin].append(numero)
        if numero % 2 == 0:
            soma_total += numero
            
        if col == 2:
            soma_terceira += numero
        
        if lin == 1 and maior_segunda < numero:
            maior_segunda = numero
        
print('-=' * 15)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[ {tabela[lin][col]} ]', end='')
    print()

print('-=' * 15)
print(f'A soma dos valores pares é {soma_total}')
print(f'A soma dos valores da terceira coluna é {soma_terceira}')
print(f'O maior valor da segunda linha é {maior_segunda}')
