from colorama import init
init()
alt = float(input('Altura da parede: '))
lar = float(input('Largura da parede: '))
area = alt * lar
tinta = area / 2

print('A sua parede tem dimenções de \033[1;33m{}m x {}m\033[m e sua área é de \033[4;32m{}m²\033[m'.format(alt, lar, area))
print('Para pintar essa parede, você precisará de \033[1;36m{} Litros de Tinta\033[m'.format(tinta))
