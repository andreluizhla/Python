frase = str(input('Digite uma frase: ')).upper().split()
frase = ''.join(frase)
palindromo = frase[::-1]
'''for c in range(len(frase) - 1, -1, -1):
    palindromo += frase[c]'''
print('A frase {} ao contrario fica: {}'.format(frase, palindromo))
if frase == palindromo:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada NÃO é um palíndromo')
