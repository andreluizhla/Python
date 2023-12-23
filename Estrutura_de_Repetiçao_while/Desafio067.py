while True:
    num = int(input('Digite um número para ver a sua tabuada (negativo para parar): '))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num * cont}')
print('Programa parado')
