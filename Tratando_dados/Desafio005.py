n = int(input('Digite um número: '))

print('O antecessor do número {} é: {}{}{}, e o sucessor desse número é: {}{}{}'.format(n, '\033[1;37;44m', n-1, '\033[m', '\033[7;37;40m', n+1, '\033[m'))
