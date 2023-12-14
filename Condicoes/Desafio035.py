a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('\033[4;32mConseguimos fazer um triângulo com essas retas\033[m')
else:
    print('\033[4;31mNão conseguimos fazer um triângulo com essas retas\033[m')
