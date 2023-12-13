cidade = str(input('Digite o nome da sua cidade: ')).strip()

print('Sua cidade tem Santo no começo do nome? \033[4;30m{}\033[m'.format(cidade[:5].upper() == 'SANTO'))
