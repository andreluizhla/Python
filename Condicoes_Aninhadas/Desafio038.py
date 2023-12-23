from colorama import init
init()
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O \033[1;33mPrimeiro valor\033[m é \033[1;34mMaior\033[m')
elif n2 > n1:
    print('O \033[1;33mSegundo valor\033[m é \033[1;34mMaior\033[m')
else:
    print('\033[1;33mNão existe\033[m valor maior, os dois são \033[1;34mIguais\033[m!')
