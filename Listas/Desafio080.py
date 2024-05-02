valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        p = 0
        while p < len(valores):
            if num <= valores[p]:
                valores.insert(p, num)
                print(f'Adicionado na posição {p} da lista...')
                break
            p += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
