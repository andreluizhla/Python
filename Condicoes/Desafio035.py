a = int(input('Digite o valor do primeiro lado: '))
b = int(input('Digite o valor do segundo lado: '))
c = int(input('Digite o valor do terceiro lado: '))

if a < b + c or b < a + c or c < a + b:
    print('Temos um triângulo')
else:
    print('Não temos um triângulo')