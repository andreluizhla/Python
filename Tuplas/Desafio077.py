tupla = ('curso', 'materia', 'python', 'tupla', 'vogal' ,
         'areio', 'pneumoultramicroscopicossilicovulcanoconiotico')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in range(0, len(tupla)):
    print(f'\nA palavra {tupla[palavra].upper()}, tem as vogais: ', end='')
    for letra in range(0, len(tupla[palavra])):
        if tupla[palavra][letra] in vogais:
            print(tupla[palavra][letra], end=' ')
print('')
