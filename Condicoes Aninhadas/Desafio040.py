n1 = float(input('Digite a sua Primeira nota: '))
n2 = float(input('Digite a sua Segunda nota: '))
media = (n1 + n2) / 2

print('Sua média foi: \033[4;34m{:.1f}\033[m'.format(media))

if media < 5:
    print('\033[1;31mREPROVADO\033[m')
elif 5 < media < 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
elif media >= 7:
    print('\033[1;32mAPROVADO\033[m')
