tabela = [[], [], []]

for lin in range(0, 3):
    for col in range(0, 3):
        numero = int(input(f'Digite um valor para [{lin}, {col}]: '))
        tabela[lin].append(numero)
        
print('-=' * 15)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[ {tabela[lin][col]} ]', end='')
    print()
