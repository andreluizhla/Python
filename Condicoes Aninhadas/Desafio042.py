from time import sleep

print('-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 10)

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

print('Analisando as retas informadas...')
sleep(3)

if a < b + c and b < a + c and c < a + b:
    print('\033[4;32mConseguimos fazer um triângulo com essas retas\033[m')
    if a == b == c:
        print('E esse triângulo é \033[4;34mEquilátero\033[m, pois ele têm \033[4;32mTODOS os 3 lados iguais\033[m')
    elif a == b or a == c or b == c:
        print('E esse triângulo é \033[4;34mIsósceles\033[m, pois ele têm \033[4;33mApenas 2 lados iguais\033[m')
    else:
        print('E esse triângulo é \033[4;34mEscaleno\033[m, pois ele \033[4;31mNÃO têm lados iguais\033[m')
else:
    print('\033[4;31mNão conseguimos fazer um triângulo com essas retas\033[m')
