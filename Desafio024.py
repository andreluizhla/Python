cidade = str(input('Digite o nome da sua cidade: '))
cidade = cidade.split()

print('Sua cidade tem Santo no começo do nome? {}'.format('Santo' in cidade[0]))
