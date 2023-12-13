t = float(input('Qual é a temperatura em °C: '))

print('A temperatura de \033[32m{}°C\033[m corresponde a \033[31m{}°F\033[m'.format(t, ((t*9)/5)+32))
