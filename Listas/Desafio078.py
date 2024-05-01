listanum = list()
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if maior < listanum[c]:
            maior = listanum[c]
        if menor > listanum[c]:
            menor = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor é {maior} e está nas posições: ', end='')
# i = posicao, item = v
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor é {menor} e está nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
print()
