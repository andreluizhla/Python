valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        valores.append(num)
    elif c == 1:
        if num > valores[0]:
            valores.append(num)
        else:
            valores.insert(0, num)
    elif c >= 2:
        if num < valores[0]:
            valores.insert(0, num)
        elif num > valores[-1]:
            valores.append(num)
        for n in range(0, len(valores)):
            if valores[n] < num < valores[n + 1]:
                valores.insert(n + 1, num)
    if valores.index(num) == valores[-1]:
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posicao {valores.index(num)} da lista...')
    print(valores)
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
