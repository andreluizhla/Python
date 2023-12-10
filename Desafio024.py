cidade = str(input('Digite o nome da sua cidade: ')).strip()

print('Sua cidade tem Santo no começo do nome? {}'.format(cidade[:5].upper() == 'SANTO'))
