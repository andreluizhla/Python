a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Conseguimos fazer um triângulo com essas retas')
else:
    print('Não conseguimos fazer um triângulo com essas retas')