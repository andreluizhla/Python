from time import sleep
print('-' * 5, 'CALCULADORA', '-' * 5)
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('\033[1;37m==\033[m' * 20)
    print('''    \033[1;36m[ 1 ] Somar\033[m
    \033[1;34m[ 2 ] Multiplicar\033[m
    \033[1;35m[ 3 ] Maior\033[m
    \033[1;32m[ 4 ] Novos Números\033[m
    \033[31m[ 5 ] Sair do Programa\033[m''')
    opcao = int(input('Digite a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('\033[1mA soma entre \033[1;34m{} e {}\033[m é \033[1;32m{}\033[m'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('\033[1mO resultado de \033[1;34m{} x {}\033[m é \033[1;32m{}\033[m'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            print('\033[1;32m{}\033[m é maior que \033[1;31m{}\033[m'.format(n1, n2))
        elif n1 < n2:
            print('\033[1;31m{}\033[m é menor que \033[1;32m{}\033[m'.format(n1, n2))
        else:
            print('\033[1;33mOs dois números são iguais\033[m')
    elif opcao == 4:
        print('\033[1;34mDigite novos números\033[m')
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
        sleep(3)
    else:
        print('\033[4;31mOpção inválida, por favor tente novamente\033[m')
print('Obrigado por usar a calculadora!')
