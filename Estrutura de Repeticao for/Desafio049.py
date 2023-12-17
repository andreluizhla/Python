num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{:2} x {} = {}'.format(c, num, num * c))
