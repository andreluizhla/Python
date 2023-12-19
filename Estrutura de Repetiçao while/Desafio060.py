num = int(input('Digite um número: '))
inputNum = num
print('{}! = {} x'.format(inputNum, num), end=' ')
fatorial = num * (num - 1)
num -= 1
while num > 1:
    print(num, end=' x ')
    fatorial *= (num - 1)
    num -= 1
print(num, end=' = ')
print(fatorial)
print('O fatorial de {} é {}'.format(inputNum, fatorial))
