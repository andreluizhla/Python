num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), 
       int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
valor9 = pares = 0
for valor in range(0, len(num)):
    if num[valor] % 2 == 0:
        pares += 1
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print(f'Foram digitados {pares} números pares')
