num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num).replace('0b', '')))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num).replace('0o', '')))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num).replace('0x', '')))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA. Tente Novamente\033[m')
