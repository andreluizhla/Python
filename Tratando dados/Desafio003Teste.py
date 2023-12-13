cor = {
    'limpa' : '\033[m',
    'verde' : '\033[1;32m',
    'amarelo' : '\033[1;33m'
    }

prinum = int(input('Escreva um número: '))

segnum = int(input('Agora, escreva outro número '))

res = prinum + segnum

print('A soma entre {}{}{} e {}{}{}, é = {}{}{}'.format(cor['amarelo'], prinum, cor['limpa'], cor['amarelo'], segnum, cor['limpa'], cor['verde'], res, cor['limpa']))
