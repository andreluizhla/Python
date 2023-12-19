cont = media = soma = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    continuar = str(input('Quer continuar? [S/N] ')).strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
