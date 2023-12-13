n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite agora, a sua segunda nota: '))

print('A média das notas \033[1;32m{:.1f}\033[m e \033[1;32m{:.1f}\033[m, é: \033[7;32;40m{:.2f}\033[m'.format(n1, n2, (n1+n2)/2) )
