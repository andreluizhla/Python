valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pass
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
