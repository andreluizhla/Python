﻿from colorama import init
init()
m = float(input('Escreva uma distância em metros: '))

print('{} metros equivale à: '.format(m))
print('{} Quilômetros'.format(m/1000))
print('{} Hectômetro'.format(m/100))
print('{} Decâmetro'.format(m/10))
print('{} Decímetro'.format(m*10))
print('{} Centímetro'.format(m*100))
print('{} Milímetro'.format(m*1000))
