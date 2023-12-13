frase = str(input('Digite uma frase: ')).upper().strip()

print('Analisando a sua frase...')

print('A letra A aparece \033[1;32m{}\033[m vezes'.format(frase.count('A')))
print('A primeira letra A aparece na posição \033[1;33m{}\033[m'.format(frase.find('A') + 1))
print('A última letra A aparece na posição \033[1;35m{}\033[m'.format(frase.rfind('A') + 1))