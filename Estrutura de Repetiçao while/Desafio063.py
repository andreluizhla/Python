enezimo = int(input('Digite quantos termos da Sequencia de Fibonacci você quer ver: '))
n1 = 0
n2 = 1
print('{}, {},'.format(n1, n2), end=' ')

while res :
    res = n1 + n2
    print(res, end=', ')
    n1 = n2
    n2 = res
print('FIM')
