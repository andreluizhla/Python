n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
n3 = int(input('Digite o Terceiro número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
    
print('O menor valor digitado foi \033[1;36m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[1;32m{}\033[m'.format(maior))
