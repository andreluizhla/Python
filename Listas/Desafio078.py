num = list()
for c in range(0, 5):
    num.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if maior < num[c]:
            maior = num[c]
        if menor > num[c]:
            menor = num[c]
print(f'Você digitou os valores {num}')
print(f'O maior valor é {maior} e está nas posições: ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{num.index(max(num))}... ', end='')
print(f'\nO menor valor é {menor} e está nas posições: ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{num.index(min(num))}... ', end='')
print()
