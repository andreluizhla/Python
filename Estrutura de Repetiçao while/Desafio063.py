enezimo = int(input('Digite quantos termos da Sequencia de Fibonacci você quer ver: '))
n1 = 0
n2 = 1
print('{}, {},'.format(n1, n2), end=' ')
cont = 3
while cont <= enezimo:
    n3 = n1 + n2
    print(n3, end=', ')
    n1 = n2
    n2 = n3
    cont += 1
print('FIM')
