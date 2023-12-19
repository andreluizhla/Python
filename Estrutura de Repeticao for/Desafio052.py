num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;31m', end='')
        total += 1
    else:
        print('\033[0;37m', end='')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('Por isso ele É PRIMO'.format(num))
else:
    print('Por isso ele NÃO É PRIMO'.format(num))
